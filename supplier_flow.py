from graphviz import Digraph

def create_supplier_workflow():
    dot = Digraph(format='png')
    
    # Define nodes
    dot.node('A', 'Order Acquisition\n(Purchase Order, Quotation, Order Confirmation)')
    dot.node('B', 'Order Processing\n(Sales Order, Production Order, Inventory Check)')
    dot.node('C', 'Manufacturing & Packaging\n(Production Report, Quality Control, Packing List)')
    dot.node('D', 'Documentation Preparation\n(Invoice, Packing List, Certificate of Origin, Export Declaration)')
    dot.node('E', 'Handover to Logistics\n(Freight Booking, Bill of Lading, Handover Receipt)')
    dot.node('F', 'Customs Clearance\n(Export Declaration, Customs Documents)')
    dot.node('G', 'Shipment Tracking\n(Tracking Reports, Transport Updates)')
    dot.node('H', 'Invoicing & Payment\n(Commercial Invoice, Payment Receipt, Reconciliation)')
    dot.node('I', 'Post-Shipment Support\n(Proof of Delivery, Complaint Reports, Archives)')
    
    # Define edges (workflow direction)
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')
    dot.edge('E', 'F')
    dot.edge('F', 'G')
    dot.edge('G', 'H')
    dot.edge('H', 'I')
    
    # Render flowchart
    dot.render('supplier_workflow', format='png', cleanup=False)
    print("Flowchart saved as supplier_workflow.png")

if __name__ == "__main__":
    create_supplier_workflow()
