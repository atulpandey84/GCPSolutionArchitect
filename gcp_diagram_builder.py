import matplotlib
matplotlib.use('Agg')  # Set non-interactive backend for headless environments
import matplotlib.pyplot as plt
import networkx as nx

def build_gcp_diagram(nodes_list, connections_list, output_filename="gcp_architecture.png"):
    """
    Builds a visual, multi-tiered multipartite layout diagram of GCP cloud components and saves it as a PNG file.
    """
    G = nx.DiGraph()

    # Define common GCP tiers for multipartite layout
    tier_mapping = {
        "Edge": 0,
        "Load Balancer": 1,
        "Network": 1,
        "Frontend": 2,
        "GKE": 3,
        "Compute": 3,
        "App": 3,
        "Processing": 4,
        "Pub/Sub": 4,
        "Data": 5,
        "Storage": 5,
        "Database": 5,
        "Security": 6,
        "IAM": 6
    }

    def get_tier(node_name):
        node_name_lower = node_name.lower()
        for keyword, tier in tier_mapping.items():
            if keyword.lower() in node_name_lower:
                return tier
        return 3  # Default middle tier

    # Add nodes with subset attribute for multipartite layout
    for node in nodes_list:
        G.add_node(node, subset=get_tier(node))

    # Add edges
    G.add_edges_from(connections_list)

    # Create the layout
    try:
        pos = nx.multipartite_layout(G)
    except Exception:
        pos = nx.spring_layout(G)

    plt.figure(figsize=(12, 8))
    nx.draw(
        G, pos, with_labels=True,
        node_color='skyblue',
        node_size=3000,
        edge_color='gray',
        arrowsize=20,
        font_size=10,
        font_weight='bold'
    )

    plt.title("GCP Enterprise Architecture", fontsize=15)
    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close()
    print(f"Diagram saved to {output_filename}")

if __name__ == "__main__":
    # Quick test
    test_nodes = ["External User", "Cloud Load Balancer", "GKE Autopilot Cluster", "Cloud Pub/Sub", "Cloud Spanner"]
    test_edges = [
        ("External User", "Cloud Load Balancer"),
        ("Cloud Load Balancer", "GKE Autopilot Cluster"),
        ("GKE Autopilot Cluster", "Cloud Pub/Sub"),
        ("Cloud Pub/Sub", "Cloud Spanner")
    ]
    build_gcp_diagram(test_nodes, test_edges, "test_gcp_arch.png")
