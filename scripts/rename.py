import os

os.chdir('/Users/alexanderboden/Documents/GitHub/SideProjects/NBA/alltimegreatgamelogs')

for f in os.listdir('/Users/alexanderboden/Documents/GitHub/SideProjects/NBA/alltimegreatgamelogs'):
    os.rename(f, f + ".csv")
