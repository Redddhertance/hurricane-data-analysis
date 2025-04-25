# hurricane-data-anlysis
Utilises an array of functions to perform various data analysis/manipulation tasks

This project analyses a dataset of major Atlantic hurricanes from 1924 to 2018. It uses basic data structures (lists, dictionaries) and custom functions to:
	Structure raw hurricane data into a usable format
	Compute statistics on hurricane frequency, severity, and impact
	Categorise hurricanes by damage and mortality ratings
  Identify the most affected regions and most devastating hurricanes

  Concepts used: functions, loops, dictionaries, lists, string parsing

Key features:
  Converts string-based monetary damages into numerical format (e.g., “1.54B” → 1.54e9)
  Combines multiple data lists into a single structured dictionary of hurricane data
  Groups hurricanes by year of occurrence
  Counts frequency of impact per geographic region
  Identifies the most frequently affected area
  Determines the most financially and humanly devastating hurricanes
  Categorises hurricanes by damage and death scales

Sample insights:
  Most frequently hit region: The Caribbean
  Most financially damaging hurricane: Katrina ($125bn)
  Hurricane with highest death toll: Mitch (19325 deaths)
  Custom 5-level scaling ratings utilised to measure both mortality and economic damage
