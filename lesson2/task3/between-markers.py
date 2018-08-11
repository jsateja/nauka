def between_markers(text: str, begin: str, end: str) -> str:
   if begin in text:
       begin_index = text.find(begin) + len(begin)
   else:
       begin_text= 0
       
   if end in text:
       end_index = text.find(end)
   else:
       end_index= len(text)
   
   return text[begin_index:end_index]



   x=re.search(begin+'(.+?)'+ end, text)
   print (x)
   if x:
        return x.group(1)
          


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
