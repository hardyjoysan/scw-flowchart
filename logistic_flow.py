from graphviz import Digraph

# Create a directed graph
flowchart = Digraph("Logistics_Workflow", format="png")
flowchart.attr(rankdir="TB", size="10")

# Nodes for Supplier
flowchart.node("PO", "Purchase Order (Buyer -> Supplier)", shape="rect", style="filled", fillcolor="lightblue")
flowchart.node("SC", "Supplier Confirmation & Proforma Invoice", shape="rect", style="filled", fillcolor="lightblue")
flowchart.node("ADV", "Advance Payment (If applicable)", shape="rect", style="filled", fillcolor="lightblue")
flowchart.node("MP", "Manufacturing & Packaging", shape="rect", style="filled", fillcolor="lightblue")
flowchart.node("SD", "Shipping Documentation (Invoice, Packing List, etc.)", shape="rect", style="filled", fillcolor="lightblue")

# Nodes for Logistics Partner
flowchart.node("FB", "Freight Booking & Pickup", shape="rect", style="filled", fillcolor="lightgreen")
flowchart.node("CH", "Cargo Handling & Warehouse Storage", shape="rect", style="filled", fillcolor="lightgreen")
flowchart.node("EXC", "Customs Export Clearance", shape="rect", style="filled", fillcolor="lightgreen")
flowchart.node("SHIP", "International Shipment & Tracking", shape="rect", style="filled", fillcolor="lightgreen")
flowchart.node("IMC", "Customs Import Clearance", shape="rect", style="filled", fillcolor="lightgreen")
flowchart.node("LMD", "Last-Mile Delivery & Warehouse Storage", shape="rect", style="filled", fillcolor="lightgreen")

# Nodes for Buyer (Consignee)
flowchart.node("VR", "Verifies Documents Before Shipment", shape="rect", style="filled", fillcolor="orange")
flowchart.node("DUTY", "Pays Import Duties (If applicable)", shape="rect", style="filled", fillcolor="orange")
flowchart.node("RECV", "Receives Goods & Inspects for Damages", shape="rect", style="filled", fillcolor="orange")
flowchart.node("PAY", "Final Payment to Supplier & Logistics", shape="rect", style="filled", fillcolor="orange")
flowchart.node("FIN", "Financial Reconciliation & Compliance Reporting", shape="rect", style="filled", fillcolor="orange")

# Connecting Nodes (Process Flow)
flowchart.edge("PO", "SC")
flowchart.edge("SC", "ADV")
flowchart.edge("ADV", "MP")
flowchart.edge("MP", "SD")
flowchart.edge("SD", "VR")
flowchart.edge("SD", "FB")
flowchart.edge("FB", "CH")
flowchart.edge("CH", "EXC")
flowchart.edge("EXC", "SHIP")
flowchart.edge("SHIP", "IMC")
flowchart.edge("IMC", "DUTY")
flowchart.edge("DUTY", "LMD")
flowchart.edge("LMD", "RECV")
flowchart.edge("RECV", "PAY")
flowchart.edge("PAY", "FIN")

# Render the flowchart
flowchart_path = "logistics_workflow"
flowchart.render(flowchart_path, format="png", cleanup=True)

# Provide the flowchart file path
flowchart_path
