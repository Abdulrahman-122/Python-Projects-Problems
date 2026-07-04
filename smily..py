# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:

#     Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
#     A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
#     Every smiling face must have a smiling mouth that should be marked with either ) or D

# No additional characters are allowed except for those mentioned.

# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]
# Example

# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

# Note
# In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.
# analysis:

# > "How many strings in the array are valid smiley faces?"

# The confusing part is the rules. Let's break them down.

# ---

# ## A smiley has 3 possible parts

# ```text
# Eyes + (optional Nose) + Mouth
# ```

# Example:

# ```text
# :-)
# ```

# Here:

# ```text
# :   -> eyes
# -   -> nose
# )   -> mouth
# ```

# ---

# ## Rule 1: Eyes

# Eyes must be **either**:

# ```text
# :
# ;
# ```

# Valid:

# ```text
# :)
# ;)
# :D
# ;D
# ```

# Invalid:

# ```text
# 8)
# xD
# A)
# ```

# because the eyes are not `:` or `;`.

# ---

# ## Rule 2: Nose (optional)

# The nose can be:

# ```text
# -
# ~
# ```

# or it can be completely absent.

# Valid:

# ```text
# :)
# :D
# :-)
# :~D
# ```

# Notice:

# ```text
# :)
# ```

# has no nose, and that's okay.

# ---

# ## Rule 3: Mouth

# The mouth must be:

# ```text
# )
# D
# ```

# Valid:

# ```text
# :)
# :D
# ;-D
# ;~)
# ```

# Invalid:

# ```text
# :(
# :[
# :}
# :>
# ```

# because `(`, `[`, `}`, `>` are not allowed mouths.

# ---

# ## Putting all rules together

# Possible valid patterns are:

# ### Without nose

# ```text
# :)
# :D
# ;)
# ;D
# ```

# ### With nose "-"

# ```text
# :-)
# :-D
# ;-)
# ;-D
# ```

# ### With nose "~"

# ```text
# :~)
# :~D
# ;~)
# ;~D
# ```

# That's all.

# ---

# ## Example 1

# ```python
# [':)', ';(', ';}', ':-D']
# ```

# Check one by one:

# ```text
# :)    -> valid
# ;(    -> invalid mouth
# ;}    -> invalid mouth
# :-D   -> valid
# ```

# Answer:

# ```text
# 2
# ```

# ---

# ## Example 2

# ```python
# [';D', ':-(', ':-)', ';~)']
# ```

# ```text
# ;D    -> valid
# :-(   -> invalid mouth
# :-)   -> valid
# ;~)   -> valid
# ```

# Answer:

# ```text
# 3
# ```

# ---

# ## Example 3

# ```python
# [';]', ':[', ';*', ':$', ';-D']
# ```

# ```text
# ;]    -> invalid mouth
# :[    -> invalid mouth
# ;*    -> invalid mouth
# :$    -> invalid mouth
# ;-D   -> valid
# ```

# Answer:

# ```text
# 1
# ```

# ---

# A useful way to think about it:

# For every string, ask:

# ```text
# 1. Does it start with : or ; ?
# 2. If there is a middle character, is it - or ~ ?
# 3. Does it end with ) or D ?
# 4. Are there any extra characters?
# ```

# If all answers are yes, count it as a smiley.

# solution:



def count_smileys(arr):
    smily_faces=0
    substring=[':)',';)',':-)',';-)',';~)',':~)',':-D',';-D',':~D',';~D',';D',':D']
    sad_faces=0
    for item in arr: 
        if item in substring:
            smily_faces+=1
        else:
            sad_faces+=1
    return smily_faces 

count_smileys([':)', ';(', ';}', ':-D']); 

#  Example

print(count_smileys([':)', ';(', ';}', ':-D'])) # should return 2;
print(count_smileys([';D', ':-(', ':-)', ';~)'])) # should return 3;
print(count_smileys([';]', ':[', ';*', ':$', ';-D'])) # should return 1;
