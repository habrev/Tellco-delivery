import streamlit as st
import pandas as pd

# Load the dataset (since it's already uploaded in the environment)
file_path = '../../assets/data/cleaned_dataset_Week2.csv'   
df = pd.read_csv(file_path)

# Ensure the dataset has the required columns (adjust as per your dataset)
tcp_downlink_column = 'TCP DL Retrans. Vol (Bytes)' 
tcp_uplink_column = 'TCP UL Retrans. Vol (Bytes)'  
rtt_columns = ['Avg RTT DL (ms)', 'Avg RTT UL (ms)'] 
throughput_columns = ['Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)']  

# Get top 10 TCP retransmissions (highest values) for both Downlink and Uplink
top_10_tcp_downlink = df[tcp_downlink_column].nlargest(10)
top_10_tcp_uplink = df[tcp_uplink_column].nlargest(10)

# Get bottom 10 TCP retransmissions (lowest values) for both Downlink and Uplink
bottom_10_tcp_downlink = df[tcp_downlink_column].nsmallest(10)
bottom_10_tcp_uplink = df[tcp_uplink_column].nsmallest(10)

# Get most frequent TCP retransmissions for both Downlink and Uplink
most_frequent_tcp_downlink = df[tcp_downlink_column].mode().head(10)
most_frequent_tcp_uplink = df[tcp_uplink_column].mode().head(10)

# --- For RTT values ---
# Get top 10 RTT (highest values)
top_10_rtt = df[rtt_columns].max().nlargest(10)

# Get bottom 10 RTT (lowest values)
bottom_10_rtt = df[rtt_columns].min().nsmallest(10)

# Get most frequent RTT
most_frequent_rtt = df[rtt_columns].mode().head(10)

# --- For Throughput values ---
# Get top 10 Throughput values (highest values)
top_10_throughput = df[throughput_columns].max().nlargest(10)

# Get bottom 10 Throughput values (lowest values)
bottom_10_throughput = df[throughput_columns].min().nsmallest(10)

# Get most frequent Throughput values
most_frequent_throughput = df[throughput_columns].mode().head(10)

# Streamlit interface
st.title('Network Performance Analysis')

# Display top TCP retransmission values
st.header('Top 10 TCP Retransmission Values')
st.subheader('Downlink')
st.write(top_10_tcp_downlink)
st.subheader('Uplink')
st.write(top_10_tcp_uplink)

# Display bottom TCP retransmission values
st.header('Bottom 10 TCP Retransmission Values')
st.subheader('Downlink')
st.write(bottom_10_tcp_downlink)
st.subheader('Uplink')
st.write(bottom_10_tcp_uplink)

# Display most frequent TCP retransmission values
st.header('Most Frequent TCP Retransmission Values')
st.subheader('Downlink')
st.write(most_frequent_tcp_downlink)
st.subheader('Uplink')
st.write(most_frequent_tcp_uplink)

# Display RTT values
st.header('RTT Analysis')

# Top 10 RTT values
st.subheader('Top 10 RTT Values')
st.write(top_10_rtt)

# Bottom 10 RTT values
st.subheader('Bottom 10 RTT Values')
st.write(bottom_10_rtt)

# Most frequent RTT values
st.subheader('Most Frequent RTT Values')
st.write(most_frequent_rtt)

# Display Throughput values
st.header('Throughput Analysis')

# Top 10 Throughput values
st.subheader('Top 10 Throughput Values')
st.write(top_10_throughput)

# Bottom 10 Throughput values
st.subheader('Bottom 10 Throughput Values')
st.write(bottom_10_throughput)

# Most frequent Throughput values
st.subheader('Most Frequent Throughput Values')
st.write(most_frequent_throughput)
