import GetSites
import maxVerts

def run_tourist_sites(capacity):
    GetSites.main(GetSites.start_address, GetSites.city)
    return maxVerts.main(capacity)


if __name__ == "__main__":
    run_tourist_sites()
