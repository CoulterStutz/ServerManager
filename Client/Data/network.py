import psutil

class Network():
    def __init__(self):
        self.interfaces = None
        self.total_interface_count = None
        self.link_status = None
        self.packets_in_total = None
        self.packets_out_total = None
        self.total_packets_in_all_interfaces = None
        self.total_packets_out_all_interfaces = None
        self.packets_in_last_second = None
        self.packets_out_last_second = None

        # Fetch total interface count
        self.interfaces = psutil.net_if_stats()
        self.total_interface_count = len(self.interfaces)

    def fetch_network_data(self):
        self.link_status = {interface: stats.isup for interface, stats in self.interfaces.items()}

        self.packets_in_total = {}
        self.packets_out_total = {}
        for interface in self.interfaces:
            counters = psutil.net_io_counters(pernic=True).get(interface)
            if counters:
                self.packets_in_total[interface] = counters.bytes_recv
                self.packets_out_total[interface] = counters.bytes_sent

        self.total_packets_in_all_interfaces = sum(self.packets_in_total.values())
        self.total_packets_out_all_interfaces = sum(self.packets_out_total.values())

        self.packets_in_last_second = {}
        self.packets_out_last_second = {}
        for interface in self.interfaces:
            last_second = psutil.net_io_counters(pernic=True).get(interface)
            if last_second:
                self.packets_in_last_second[interface] = last_second.bytes_recv
                self.packets_out_last_second[interface] = last_second.bytes_sent

    def return_network_data(self):
        self.fetch_network_data()

        return {
            "TotalInterfaceCount": self.total_interface_count,
            "Interfaces": self.interfaces,
            "LinkStatus": self.link_status,
            "PacketsInTotal": self.packets_in_total,
            "PacketsOutTotal": self.packets_out_total,
            "TotalPacketsInAllInterfaces": self.total_packets_in_all_interfaces,
            "TotalPacketsOutAllInterfaces": self.total_packets_out_all_interfaces,
            "PacketsInLastSecond": self.packets_in_last_second,
            "PacketsOutLastSecond": self.packets_out_last_second
        }

# Example usage
if __name__ == '__main__':
    network = Network()
    print(network.return_network_data())
