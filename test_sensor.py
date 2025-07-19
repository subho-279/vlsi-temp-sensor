import pandas as pd

def test_voltage_range():
    df = pd.read_csv("ptat_output.csv", sep='\s+', comment="*", header=None)
    
    # Print a sample of the first row to verify column layout (debug)
    print(df.head())

    # Check how many columns are present
    assert df.shape[1] >= 4, "CSV doesn't have enough columns"

    # Assign column names dynamically based on number of columns
    df.columns = ["Temp_C", "V_PTAT", "V_CTAT", "V_OUT"][:df.shape[1]]

    # Validate voltage ranges
    assert df["V_PTAT"].between(0.4, 1.5).all(), "V_PTAT out of expected range"
    assert df["V_CTAT"].between(0.3, 1.2).all(), "V_CTAT out of expected range"
    assert df["V_OUT"].between(0.5, 2.0).all(), "V_OUT out of expected range"