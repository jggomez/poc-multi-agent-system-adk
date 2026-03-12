1. **Evaluation Criteria:**
* Determine if the available data is **Dissolved CO2** ($mg/l$) for liquid samples or **Partial Pressure ($P_{p}$)** for the gas phase.
* Calculate Partial Pressure if only the molar fraction is available: $P_{p} = \text{Molar Fraction} \times \text{Maximum Operating Pressure}$.

2. **Score Classification (Table 12):**
* **Gas Phase ($P_{p}$ CO2):**
* $< 3$ psi: **0 points** (Inert/Non-corrosive).
* $3$ to $30$ psi: **8 points** (Moderate corrosion).
* $> 30$ psi: **14 points** (Corrosive).

* **Liquid Phase (Dissolved CO2):**
* $< 250$ mg/l: **0 points**.
* $250 - 1500$ mg/l: **8 points**.
* $> 1500$ mg/l: **14 points**.

3. **Handling Missing Data (s/d):**
* If the technical data is unknown or not provided (s/d), automatically assign **10 points** (This represents the mandatory 70% of the 14-point maximum).

4. **Generation of Recommendations:**
* **Scores > 8:** Recommend strict pH monitoring and the injection of corrosion inhibitors specifically formulated for carbonic acid (sweet corrosion).
* **Score 14:** Classified as high criticality; suggest direct inspection or the use of corrosion coupons to verify the actual metal loss rate.
* **s/d (Unknown):** Urgently request a gas chromatography or formation water analysis to eliminate the uncertainty penalty and accurately assess the risk.

## Examples

**Example 1: High Pressure Gas Phase**

* **Input:** Operating pressure 800 psi, CO2 content 5%.
* **Calculation:** $P_{p} = 800 \times 0.05 = 40$ psi.
* **Analysis:** According to Table 12, 40 psi > 30 psi. Score: **14 points**.
* **Recommendation:** The fluid is highly corrosive due to CO2 partial pressure. It is recommended to verify internal coating integrity (if applicable) and ensure the continuity and dosage of the film-forming corrosion inhibitor.

**Example 2: Unknown Data (s/d)**

* **Input:** The operator has not provided fluid composition analysis for the segment.
* **Analysis:** Data not available (s/d). Assign uncertainty score: **10 points**.
* **Recommendation:** Schedule a fluid sampling during the next operational window to determine the CO2 molar fraction. This will allow the risk model to be updated with real data and potentially reduce the penalized score.