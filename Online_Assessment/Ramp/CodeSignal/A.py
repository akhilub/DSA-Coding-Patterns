import json
import re

def solution(jsonData):
    # Parse the JSON data
    data = json.loads(jsonData)
    
    # Function to determine the correct number of bedrooms
    def get_correct_bedrooms(description, num_bedrooms):
        description = description.lower()
        
        # Check for studio
        if re.search(r'\b(?<!yoga\s)(?<!dance\s)(?<!art\s)studio\b', description):
            return 0
        
        # Check for 1-bedroom
        if re.search(r'\b(?<!yoga\s)(?<!dance\s)(?<!art\s)1-bedroom\b', description) or \
           re.search(r'\b(?<!yoga\s)(?<!dance\s)(?<!art\s)one bedroom\b', description):
            return 1
        
        # If no match found, return the original value
        return num_bedrooms

    # Process each listing and correct num_bedrooms
    corrected_bedrooms = []
    for listing in data:
        description = listing['description']
        num_bedrooms = listing['num_bedrooms']
        
        corrected_num_bedrooms = get_correct_bedrooms(description, num_bedrooms)
        corrected_bedrooms.append(corrected_num_bedrooms)
    
    return corrected_bedrooms
