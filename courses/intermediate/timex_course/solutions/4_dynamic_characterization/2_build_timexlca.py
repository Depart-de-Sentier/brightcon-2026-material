from datetime import date

from bw_timex import TimexLCA
demand = {("test", "A"): 1}
gwp = ("GWP", "example")

tlca = TimexLCA(demand, gwp)
tlca.build_timeline(starting_datetime = date(2026, 9, 16), temporal_grouping="day") #starting date of the timeline
tlca.lci()
tlca.static_lcia()
