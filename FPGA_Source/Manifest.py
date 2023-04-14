target = "radiant"
action = "synthesis"

syn_family = "LIFCL"
syn_device = "17"
syn_grade = "9"
syn_package = "BG256I"
syn_top = "mipi_bridge"
syn_project = "mipi_bridge"
syn_tool = "radiant_synp"

modules = {"local" : [
                    "mipi_csi_phy",
                    "out_line_ram_ldp",
                    "source/mipi_csi_bridge",
                    "oscillator",
                    "out_line_ram_dp",
                    "out_line_ram_ldp",
                    "line_ram_dp"]
          }
files = [
    "mipi_csi_bridge.ldc",
    "mipi_csi_bridge.pdc"
]
