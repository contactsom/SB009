print("***************START: String Example - Formatting String ***************")

simplilearnHeading="1000 of our learners achieve their goal"
print(simplilearnHeading)

print("-------------------------")

print('%(totallearners)d of our learners achieve their goal'
        %{"totallearners":1000}
      )

print("-------------------------")

# Simplilearn is INDIA no 1 PYTHON training Portal

print('%(edtech)s is %(country)s no %(rank)d %(course)s training Portal'

      % {"edtech": "Simplilearn","country": "INDIA","rank":1,"course":"PYTHON" }

      )

print("-------------------------")

#200+ Hiring Partners in Simplilearn

simplilearntag="{} Hiring Partners in Simplilearn"
hiringPartners=200

print(simplilearntag.format(hiringPartners))

print("-------------------------")

# Simplilearn is INDIA no 1 PYTHON training Portal

simplilarnportal="{edtech} is {country} no {rank} {course} training Portal"

print(simplilarnportal.format(edtech="Simplilearn", country= "INDIA", rank= 1, course= "PYTHON"))


print("***************END: String Example - Formatting String ***************")