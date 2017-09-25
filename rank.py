class Legislator:
    def __init__(self, congress, icpsr, state_code, district, state, party, name, dim1, dim2, dim1bootstrappedstandarderror, dim2bootstrappedstandarderror, correlation, loglikelihood, votes, errors, geomeanprobability):
        self.congress = congress
        self.icpsr = icpsr
        self.state_code = state_code
        self.district = district
        self.state = state
        self.party = party
        self.name = name
        self.dim1 = dim1
        self.dim2 = dim2
        self.dim1bootstrappedstandarderror = dim1bootstrappedstandarderror
        self.dim2bootstrappedstandarderror = dim2bootstrappedstandarderror
        self.correlation = correlation
        self.loglikelihood = loglikelihood
        self.votes = votes
        self.errors = errors
        self.geomeanprobability = geomeanprobability

    def to_csv(self):
        return(",".join([str(x) for x in [self.congress, self.icpsr, self.state_code, self.district, self.state, self.party, self.name, self.dim1, self.dim2, self.dim1bootstrappedstandarderror, self.dim2bootstrappedstandarderror, self.correlation, self.loglikelihood, self.votes, self.errors, self.geomeanprobability]]) + "\n")

# load source data
from openpyxl import load_workbook
data = load_workbook('data/data.xlsx').active

congresses = {}

for row in data.rows:
    legislator = Legislator(*[value.value for value in row])
    # print dir(legislator.state.value)
    if legislator.state == 'USA':
        continue # exclude Presidents
    if str(legislator.congress) not in congresses:
        congresses[str(legislator.congress)] = []
    congresses[str(legislator.congress)].append(legislator)

for congress_name in congresses:
    congress = congresses[congress_name]
    by_votes = sorted(congress, key=lambda k: k.votes, reverse=True)
    by_conservatism = sorted(by_votes[:100], key=lambda k: k.dim1, reverse=True)
    with open("congresses/" + congress_name + ".csv", "wb") as outfile:
        outfile.write("congress,icpsr,state_code,district,state,party,name,dim1,dim2,dim1bootstrappedstandarderror,dim2bootstrappedstandarderror,correlation,loglikelihood,votes,errors,geomeanprobability\n")
        for legislator in by_conservatism:
            outfile.write(legislator.to_csv())
