
### Data utils ###

zips = {
    94501: "Alameda A/B-2",
    94502: "Alameda B-2",
    94514: "Byron A-1",
    94536: "Fremont D-4",
    94538: "Fremont D-5",
    94539: "Fremont E-5", 
    94541: "Cherryland/Hayward C-3",
    94542: "Hayward C/D-3",
    94544: "Hayward C-4",
    94545: "Hayward C-3",
    94546: "Castro Valley C-3",
    94550: "Livermore F-3a",
    94551: "Livermore F-3b", 
    94552: "Castro Valley C/D-3",
    94555: "Fremont C-4", 
    94560: "Newark C/D-5", 
    94566: "Pleasanton E-3a", 
    94568: "Dublin D/E-3", 
    94577: "San Leandro B/C-3", 
    94578: "San Leandro C-3", 
    94579: "San Leandro B/C-3", 
    94580: "San Lorenzo B/C-3", 
    94586: "Sunol E-4", 
    94587: "Union City C/D-4",
    94588: "Pleasanton E-3b", 
    94601: "Oakland B-2a", 
    94602: "Oakland/Piedmont B-2b", 
    94603: "Oakland B-2c", 
    94605: "Oakland C-2", 
    94606: "Oakland B-2d", 
    94607: "Oakland A-2", 
    94608: "Emeryville/Oakland A-1", 
    94609: "Oakland B-1a", 
    94610: "Piedmont B-1/2", 
    94611: "Piedmont B-1", 
    94612: "Oakland B-2e",
    94613: "Mills College B-2", 
    94618: "Oakland B-1b", 
    94619: "Oakland B/C-2", 
    94621: "Okland B-2f", 
    94702: "Berkeley A-1a", 
    94703: "Berkeley A/B-1a", 
    94704: "Berkeley B-1a", 
    94705: "Berkeley B-1b", 
    94706: "Albany A-1", 
    94707: "Berkeley A/B-1b", 
    94708: "Berkeley B-1c", 
    94709: "Berkeley B-1d",
    94710: "Berkeley A-1b", 
    94720: "Berkeley A-1c", 
    95391: "Tracy A-1"
}






### Graph utils ###


# Adds edges to 
def edges(G, u, v):
    G.add_edge(u, v)
    G.add_edge(v, u)
    return

