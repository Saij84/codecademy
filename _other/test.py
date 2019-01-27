author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {} by {} was originally published in {} in {}.".format(publishing_date, author, title, original_work)
  return poem_desc

print(poem_description(publishing_date, author, title, original_work))

