def cases(issues):
     match issues:
      case "Dot-com bubble burst (2000-2002)":
       return 3.2/100
      case "September 11th attacks (2001)":
       return 3/100
      case "Enron scandal (2001)":
       return 0
      case "Iraq War (2003-2011)":
       return 5/100
      case ("Subprime mortgage crisis" | "Great Recession (2007-2009)"):  # Match multiple options
       return 1/100
      case "European sovereign debt crisis (2010-2012)":
       return 4/100
      case "COVID-19 pandemic (2020-2023)":
       return 7/100
      case _:
       return 0