### Image processing utils ###

def PrintArrayInfo(a):
    print("Array info:")
    print("shape", a.shape)
    print("dtype:", a.dtype)
    print("min, max", a.min(), a.max())


### Data utils ###

cities = [
    "Alameda",
    "Albany",
    "Berkeley",
    "Castro Valley",
    "Dublin",
    "Emeryville",
    "Fremont",
    "Hayward",
    "Livermore",
    "Newark",
    "Oakland",
    "Pleasanton",
    "San Leandro",
    "San Lorenzo",
    "Sunol",
    "Union City"
]

zips_original = {
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
    94621: "Okland", 
    94702: "Berkeley", 
    94703: "Berkeley", 
    94704: "Berkeley", 
    94705: "Berkeley", 
    94706: "Albany", 
    94707: "Berkeley", 
    94708: "Berkeley", 
    94709: "Berkeley",
    94710: "Berkeley", 
    94720: "Berkeley", 
    # 95391: "Tracy"
}

zips = {
    94501: "Alameda",
    94502: "Alameda",
    94514: "Alameda",
    94536: "Fremont",
    94538: "Fremont",
    94539: "Fremont", 
    94541: "Hayward",
    94542: "Hayward",
    94544: "Hayward",
    94545: "Hayward",
    94546: "Castro Valley",
    94550: "Livermore",
    94551: "Livermore", 
    94552: "Castro Valley",
    94555: "Fremont", 
    94560: "Newark", 
    94566: "Pleasanton", 
    94568: "Dublin", 
    94577: "San Leandro", 
    94578: "San Leandro", 
    94579: "San Leandro", 
    94580: "San Lorenzo", 
    94586: "Sunol", 
    94587: "Union City",
    94588: "Pleasanton", 
    94601: "Oakland", 
    94602: "Oakland", 
    94603: "Oakland", 
    94605: "Oakland", 
    94606: "Oakland", 
    94607: "Oakland", 
    94608: "Emeryville", 
    94609: "Oakland", 
    94610: "Oakland", 
    94611: "Oakland", 
    94612: "Oakland",
    94613: "Oakland", 
    94618: "Oakland", 
    94619: "Oakland", 
    94621: "Oakland", 
    94702: "Berkeley", 
    94703: "Berkeley", 
    94704: "Berkeley", 
    94705: "Berkeley", 
    94706: "Albany", 
    94707: "Berkeley", 
    94708: "Berkeley", 
    94709: "Berkeley",
    94710: "Berkeley", 
    94720: "Berkeley", 
    # 95391: "Tracy"
}


### Graph utils ###


# Adds edges to 
def edges(G, u, v):
    G.add_edge(u, v)
    G.add_edge(v, u)
    return

