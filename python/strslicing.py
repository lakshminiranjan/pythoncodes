#slicing---creating  a substring by extracting the elements of other strings
#                 indexing[] or slice()
#                 [start:stop:step]-->start is inclusive and stop is exclusive
#step is how much we are increasing our index at starting and stopping

# name = "Niranjan Nizy"

# first_name = name[:8]
# last_name  = name[9:]#if user leaves empty python assumes it as a end or start
# funky_name = name[::2]#displays only the seconf character
# rev_name = name[::-1]-->reversea str in python using slicing

# print(first_name+" "+last_name+" "+funky_name+" "+rev_name)

website1 = "https://www.google.com"
website2 = "https://www.instagram.com"

slice = slice(12,-4)

print(website1[slice]+" "+website2[slice])

