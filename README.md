# Clusterize
# Language: Python
# Input: prefix (for CSV files for network and clusters)
# Output: CSV (network with only edges between nodes in the same cluster)
# Tested with: PluMA 1.1, Python 3.6
# Dependency: CSV2GML Plugin

PluMA plugin which takes a CSV file representing a network and removes all edges between
nodes in different clusters.
This can be useful for any downstream cluster-based analysis, either studying properties of each 
cluster or more clearly visualizing the network.

The input is a prefix.  The network CSV file is assumed to be (prefix).csv and the cluster
CSV file is assumed to be (prefix).clusters.csv.

The expected format for the network CSV file is for rows and columns to hold node names, and for
entry (i, j) to hold the weight of the edge from node i to node j.

The clusters CSV format should be as follows:
"","x"
"1","Family.Lachnospiraceae.0001"
"2","Family.Ruminococcaceae.0003"
"3","Family.Lachnospiraceae.0029"
"4","Family.Lachnospiraceae.0043"
"5","Family.Ruminococcaceae.0019"
"6","Family.Lachnospiraceae.0095"
"","x"
"1","Family.Porphyromonadaceae.0005"
"2","Family.Porphyromonadaceae.0006"
"3","Family.Lachnospiraceae.0045"
"4","Order.Clostridiales.0007"
"","x"
"1","Kingdom.Bacteria.0001"
"2","Family.Porphyromonadaceae.0013"
"3","Phylum.Firmicutes.0004"

The output CSV file will then be the same as the input network CSV file, but with all edges (i', j')
between any nodes i' and j' not in the same cluster removed.
