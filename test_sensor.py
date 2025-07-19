import pandas as pd

def test_voltage_range():
    df = pd.read_csv("ptat_output.csv", sep=r'\s+', comment="*", header=None)

    # Use only the columns we care about (every second value)
    df_clean = pd.DataFrame({
        "Temp_C": df[0],
        "V_PTAT": df[1],
        "V_CTAT": df[3],
        "V_OUT": df[5]
    })

    # Validate voltage ranges
    assert df_clean["V_PTAT"].between(0.4, 1.5).all(), "V_PTAT out of expected range"
    assert df_clean["V_CTAT"].between(0.3, 1.2).all(), "V_CTAT out of expected range"
    assert df_clean["V_OUT"].between(0.5, 2.0).all(), "V_OUT out of expected range"