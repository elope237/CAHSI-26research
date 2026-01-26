# Interactive FFT demo with a slider to change frequency (Hz) live
# Run: python fft_slider_demo.py
# Needs: pip install numpy matplotlib
""" Use Zoom/Pan tool to zoom into FFT plot for better visibility """ 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def compute_fft_mag(x, fs):
    X = np.fft.rfft(x)
    freqs = np.fft.rfftfreq(len(x), d=1.0 / fs)
    mag = np.abs(X) / len(x)
    return freqs, mag


def make_sine(t, hz, amp):
    return amp * np.sin(2 * np.pi * hz * t)


def main():
    # Sampling setup
    fs = 1000          # samples/sec
    duration = 1.0     # seconds
    t = np.arange(0, duration, 1.0 / fs)

    # Initial params
    hz0 = 50.0
    amp0 = 1.0

    x = make_sine(t, hz0, amp0)
    freqs, mag = compute_fft_mag(x, fs)

    # Bigger figure + better spacing
    fig, (ax_time, ax_fft) = plt.subplots(2, 1, figsize=(12, 7))

    # Reserve enough bottom for 2 sliders, plus extra top room for suptitle
    fig.subplots_adjust(left=0.10, right=0.98, top=0.88, bottom=0.22, hspace=0.45)

    # Time-domain line
    (line_time,) = ax_time.plot(t, x, lw=1)
    ax_time.set_title("Time Domain Signal", pad=8)
    ax_time.set_xlabel("Time (s)", labelpad=6)
    ax_time.set_ylabel("Amplitude")
    ax_time.grid(True, alpha=0.25)

    # Frequency-domain line
    (line_fft,) = ax_fft.plot(freqs, mag, lw=1)
    ax_fft.set_title("FFT Magnitude Spectrum", pad=8)
    ax_fft.set_xlabel("Frequency (Hz)", labelpad=6)
    ax_fft.set_ylabel("Magnitude")
    
    ax_fft.set_xlim(0, 350) # limit x-axis to 250 Hz for better visibility
    ax_fft.grid(True, alpha=0.25)

    # Slider axes (moved slightly lower + thinner so they fit cleanly)
    left = 0.12
    width = 0.78
    ax_hz = fig.add_axes([left, 0.11, width, 0.03])
    ax_amp = fig.add_axes([left, 0.06, width, 0.03])
    
    # Sliders
    # change valmax and valstep for finer control
    hz_slider = Slider(ax=ax_hz, label="Frequency (Hz)", valmin=1, valmax=350, valinit=hz0, valstep=1)
    amp_slider = Slider(ax=ax_amp, label="Amplitude", valmin=0.1, valmax=2.0, valinit=amp0, valstep=0.1)

    # Update function called whenever slider moves
    def update(_):
        hz = hz_slider.val
        amp = amp_slider.val

        x_new = make_sine(t, hz, amp)
        freqs_new, mag_new = compute_fft_mag(x_new, fs)

        line_time.set_ydata(x_new)
        line_fft.set_ydata(mag_new)

        # Keep y-limits reasonable as amplitude changes
        ax_time.set_ylim(-2.2, 2.2)
        ax_fft.set_ylim(0, max(0.001, float(mag_new.max()) * 1.15))

        fig.canvas.draw_idle()

    hz_slider.on_changed(update)
    amp_slider.on_changed(update)

    fig.suptitle(
        "Interactive FFT: Move the slider to change Hz and watch the spectrum shift",
        fontsize=14,
        y=0.97,  # lift the suptitle a bit
    )

    plt.show()


if __name__ == "__main__":
    main()
