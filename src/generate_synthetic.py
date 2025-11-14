"""
Synthetic dataset generator for the high school graduation project.

This script creates a de-identified, fully synthetic dataset with a schema
similar to a typical graduation/attendance model. It is safe for public use
and can be used to run the notebook end-to-end.
"""

import numpy as np
import pandas as pd
import os


def generate_synthetic_education_data(n=2000, seed=42):
    rng = np.random.default_rng(seed)

    grade_level = rng.integers(9, 13, n)  # 9–12
    gpa = rng.normal(2.8, 0.6, n).clip(0.0, 4.0)
    attendance_rate = rng.normal(0.92, 0.05, n).clip(0.5, 1.0)
    credits_earned = rng.integers(0, 28, n)
    discipline_incidents = rng.poisson(0.4, n)
    ela_score = rng.normal(250, 20, n)
    math_score = rng.normal(250, 22, n)
    ell_flag = rng.binomial(1, 0.12, n)
    sped_flag = rng.binomial(1, 0.14, n)
    frl_flag = rng.binomial(1, 0.55, n)

    # underlying logit for on-time graduation
    logit_grad = (
        3.0 * attendance_rate +
        0.9 * (gpa - 2.0) +
        0.1 * (credits_earned - 18) -
        0.7 * (discipline_incidents > 1) +
        0.01 * (ela_score - 240) +
        0.012 * (math_score - 240) -
        0.3 * frl_flag -
        0.2 * ell_flag -
        0.2 * sped_flag -
        2.0
    )
    p_grad = 1 / (1 + np.exp(-logit_grad))
    on_time_grad = rng.binomial(1, p_grad)

    # regular attendance target
    logit_att = (
        4.0 * attendance_rate +
        0.5 * (gpa - 2.0) -
        0.3 * frl_flag -
        0.2 * ell_flag -
        2.5
    )
    p_att = 1 / (1 + np.exp(-logit_att))
    regular_attendance = rng.binomial(1, p_att)

    df = pd.DataFrame({
        "grade_level": grade_level,
        "gpa": gpa.round(2),
        "attendance_rate": attendance_rate.round(3),
        "credits_earned": credits_earned,
        "discipline_incidents": discipline_incidents,
        "ela_score": ela_score.round(1),
        "math_score": math_score.round(1),
        "ell_flag": ell_flag,
        "sped_flag": sped_flag,
        "frl_flag": frl_flag,
        "on_time_graduation": on_time_grad,
        "regular_attendance": regular_attendance
    })
    return df


if __name__ == "__main__":
    df = generate_synthetic_education_data(n=2000, seed=42)
    os.makedirs("data", exist_ok=True)
    out_path = os.path.join("data", "synthetic_graduation_data.csv")
    df.to_csv(out_path, index=False)
    print(f"Wrote {out_path} with shape", df.shape)
