# Corporate Banking Secure Data Flow Optimization

## 1. Real-World Problem Context
In corporate banking, massive amounts of critical data must be securely transferred between regional hubs and the main headquarters. 

## 2. Problem Definition
The bank's IT team needs to determine the absolute maximum data bandwidth (in Mbps) that can be securely routed from the Istanbul Data Center (`Istanbul_DC`) to the Anadolu Headquarters (`Anadolu_HQ`) without exceeding the capacity of any single connection.

## 3. Network Model
This problem is formulated as a **Maximum Flow Problem**. 

## 4. Nodes and Edges
* **Nodes (6):** Represent the bank's data centers (`Istanbul_DC`, `Ankara_Hub`, `Izmir_Hub`, `Bursa_Hub`, `Antalya_Hub`, `Anadolu_HQ`).
* **Edges (8):** Represent the secure fiber optic links. The edge attribute is `capacity` measured in Mbps.

## 5. Selected Algorithm
The Maximum Flow algorithm is utilized via NetworkX.

## 6. Python Implementation
The project uses `pandas` for data manipulation, `networkx` for graph building and algorithm calculation, and `matplotlib` for network visualization.

## 7. Results
* **Maximum Flow:** 1600 Mbps

## 8. Managerial Interpretation
The results indicate a bottleneck approaching the headquarters. Although the source can transmit 1800 Mbps, only 1600 Mbps reaches the HQ. The `Bursa_Hub` receives 900 Mbps from Ankara and Izmir combined, but its link to the HQ is capped at 700 Mbps. **Strategic Decision:** The bank's next infrastructure investment should prioritize upgrading the fiber link between `Bursa_Hub` and `Anadolu_HQ`.

## 9. How to Run the Code
1. Install requirements: `pip install -r requirements.txt`
2. Navigate to src folder: `cd src`
3. Run the script: `python solution.py`

## 10. References
1. NetworkX Documentation.
2. MIS Network Optimization Projects Lecture Slides.
