import pandas as pd

def test_voltage_range():
    df = pd.read_csv("ptat_output.csv", delim_whitespace=True, comment="*", header=None)
    df.columns = ["Index", "Temp_C", "V_PTAT", "V_CTAT", "V_OUT", "Dummy"]

    assert df["V_PTAT"].between(0.4, 1.5).all(), "V_PTAT out of expected range"
    assert df["V_CTAT"].between(0.4, 1.5).all(), "V_CTAT out of expected range"
    assert df["V_OUT"].between(0, 5.0).all(), "V_OUT out of expected range"