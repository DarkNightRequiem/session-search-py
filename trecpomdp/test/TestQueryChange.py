if __name__ == '__main__':
    qPre= "nickname for france football team in world cup 1998"
    qNow= "stadium final world cup 1998"

    # 去掉首尾的空格并将一些特殊字符去掉
    q1=qPre.strip().replace("\"", "").replace(".", "").replace(";", "").replace("&", "").replace(":", "")
    q2=qNow.strip().replace("\"", "").replace(".", "").replace(";", "").replace("&", "").replace(":", "")

    # 进行分割
    a1=q1.split(" ")
    a2=q2.split(" ")

    # 记录A R K
    aList=[]
    rList=[]
    kList=[]

    for term in a1:
        if term in q2:
            # 找 k
            kList.append(term)
            q1.replace(term,"")
            q2.replace(term,"")
        elif term not in q2:
            # 找 R
            rList.append(term)
    # 找A
    for term in a2:
        if term not in q1:
            aList.append(term)

    print("A: ",aList,"\n","R: ",rList,"\n","K: ",kList)

    print("That is ok")




"""
self-regulating house temperature
passive solar cooling
passive solar cooling :uk
radiant barrier
radiant barrier :uk
gun homicides australia
martin bryant port arthur massacre
port arthur massacre
port arthur massacre australia
gun homicides australia after 1996
bollywood
bollywood stars
bollywood beverly hills
bollywood oscars
world film industries
collagen vascular disease
impact of collagen vascular disease
collagen vascular disease active lifestyle
collagen vascular disease sport
"collagen vascular disease" sport
"collagen vascular disease" 
when france win world cuo
when france win world cup
france versus who world cup 1998
france versus who world cup 1998 final score
nickname for france football team in world cup 1998
stadium final world cup 1998
coach france football team world cup 1998
dehumidifiers
dehumidifiers things to condiser
dehumidifiers things to consider
dehumidifiers technical specifications
dehumidifiers technical specifications uk
403(b) retirement plan
personal IRA
personal IRA v 403 (b)
personal IRA or 403 (b)
help retirement plan
silicon roof coating
silicon roof coating use
silicon roof coating tutorial
roof coating tutorial
roof coating solutions
roof coating lower temperature
Sunspots Wikipedia
Sunspots Environmental effects
Sunspot life cycle
Are sunspots local burnouts
How do sunspots effect us
psuedocyesis
psuedocyesis causes
psuedocyesis causes research
psuedocyesis causes study
psuedocyesis pathogenesis
psuedocyesis pathology
merck &amp; co. lobbying
merck &amp; co. lobbying
merck and co. lobbying
merck and co
merck and co policies
water turbines
water turbines relation to newtons law
water turbines replace fossil fuels
water turbines electricity generation cost per kWh 
effective water turbines types
comparison of water turbine types
"connecticut fire academy"
"connecticut fire academy" wiki
"connecticut fire academy" fireman
"Connecticut Fire Academy" fireman
"Connecticut Fire Academy"
SUNY colleges
SUNY albany hospital location
"SUNY albany hospital" location
"SUNY albany hospital" location
albany university hospital location
SUNY plattsburgh athletics
tax junk food benefits
tax junk food benefits un
tax junk food benefits UN evidence
high calorie food tax evidence based
high calorie snack tax evidence based
government intervention tax "junk food"
Boston Pops
Define: Boston Pops
Conductor of the boston pops orchestra
Conductor 2012 of the boston pops orchestra
Information regarding the Boston Pops Conductor
Information regarding the Boston Pops Manager
venture capital
loans for entrepreneurship
loans for entrepreneurship switzerland
loans for business
loans for business us government
renting a building business sillicon valley
renting an office sillicon valley
eurozone portugal leader actions
eurozone spain leader actions
spain spanish leader crisis action
ireland spanish leader crisis action
ireland irish leader crisis action
piigs leader crisis action
cyprus leader crisis action
long-term care insurance
long term care insurance
long term care insurance uk
long term care insurance uk \u00a3
long term care insurance "united kingdom" OR britain OR england
long term care insurance -usa
suny colleges names
number of suny colleges
suny college bioinformatics degree
map suny albany hospital
map "albany hospital" ny
patent filing
patent filing
patent office
patent law
patent law uk
patent lawyer
provisional patent
legality alcohol marijuana
legality alcohol marijuana history
legality alcohol history
legality alcohol history maijuana
legality alcohol history marijuana
why is marijuana illegal?
is marijuana worse for your health than alcohol?
gun control opinions
gun control us government
gun control current affairs
gun control current affairs
gun violence us
law center to prevent gun violence
how to quit smoking 
quiting smoking side effecs
quiting smoking side effects
quiting smoking using hypnosis
quiting smoking help
infant development cultural differences
infant development western eastern cultures
infant development milestone cultural effects
infant development milestone "cultural differences"
infant development milestone "cultural competence
infant development milestone developed and third world countries
JP Morgan Chase data centres
JP Morgan Chase data centres vs google
JP Morgan Chase computational scientist profile
JP Morgan computational scientist profile
JP Morgan data center news
phd business jobs
phd business salaries
business phd funding
business phd vs masters
business phd duration
business phd income
HIV Africa charity medicine
HIV Africa charity
HIV Africa charity donate
AIDS Africa charity donate
malaria Africa charity donate
policies for addressing economic problems in europe
'EUROPEAN UNION" "ECONOMIC CRISIS"
'EUROPEAN UNION" "ECONOMIC CRISIS" greece
'EUROPEAN UNION" "ECONOMIC CRISIS" portugal
'EUROPEAN UNION" "ECONOMIC CRISIS" spain
road trip
best road trips
best worst road trips
romantic road trips
enjoyable boring road trip
enjoyable boring getaways
best getaways
jp morgan data centers
jp morgan data
jp morgan data centers investment
jp morgan largest data center
data center compare microsoft jp morgan
dulles airport
dulles airport location
dulles hotels
dulles hotels
dulles hotels
dulles hotels
dulles metro stop
"""
