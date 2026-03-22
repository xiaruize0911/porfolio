#!/usr/bin/env python3
"""Create updated qualitative figures from current best-checkpoint GIFs."""

from pathlib import Path
from typing import List

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image, ImageSequence

ROOT = Path("/teamspace/studios/this_studio")
FIG_DIR = ROOT / "text2sign_paper" / "figures"
GEN_DIR = ROOT / "text_to_sign" / "generated_eval_best_20260320"


def load_frames(path: Path, num_frames: int = 8) -> List[Image.Image]:
    gif = Image.open(path)
    frames = [frame.convert("RGB") for frame in ImageSequence.Iterator(gif)]
    if not frames:
        raise ValueError(f"No frames found in {path}")
    if len(frames) <= num_frames:
        return frames
    indices = [round(i * (len(frames) - 1) / (num_frames - 1)) for i in range(num_frames)]
    return [frames[i] for i in indices]


def make_single_strip(gif_path: Path, out_path: Path, title: str) -> None:
    frames = load_frames(gif_path, num_frames=8)
    fig, axes = plt.subplots(1, len(frames), figsize=(12, 2.0))
    for ax, frame, idx in zip(axes, frames, range(len(frames))):
        ax.imshow(frame)
        ax.axis("off")
        ax.set_title(f"F{idx+1}", fontsize=8)
    fig.suptitle(title, fontsize=11)
    plt.tight_layout()
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def make_two_prompt_comparison(gif_a: Path, gif_b: Path, out_path: Path) -> None:
    frames_a = load_frames(gif_a, num_frames=6)
    frames_b = load_frames(gif_b, num_frames=6)
    fig, axes = plt.subplots(2, 6, figsize=(9, 3.4))
    for j, frame in enumerate(frames_a):
        axes[0, j].imshow(frame)
        axes[0, j].axis("off")
        if j == 0:
            axes[0, j].set_ylabel("Hello", fontsize=10)
    for j, frame in enumerate(frames_b):
        axes[1, j].imshow(frame)
        axes[1, j].axis("off")
        if j == 0:
            axes[1, j].set_ylabel("Thank you", fontsize=10)
    fig.suptitle("Best-checkpoint qualitative generations (8 DDIM steps, CFG=5.0)", fontsize=11)
    plt.tight_layout()
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    hello = GEN_DIR / "sign_0_Hello.gif"
    thank_you = GEN_DIR / "sign_1_Thank_you.gif"

    make_single_strip(
        hello,
        FIG_DIR / "generated_sample.png",
        "Current best checkpoint: Hello (8-step DDIM, CFG=5.0)",
    )
    make_two_prompt_comparison(
        hello,
        thank_you,
        FIG_DIR / "comparison_training_fixed.png",
    )


if __name__ == "__main__":
    main()
