# Config file with configparser

**Methods:**

**add_section**(section)- Create a new section in the configuration.

**defaults()**
**get(section)**-   Get an option value for a given section.
**getfloat**(section, option, **kwargs)
**getint**(section, option, *,  **kwargs)
**has_option**(section, option) -   Check for the existence of a given option in a given section.
                                If the specified `section’ is None or an empty string, DEFAULT is assumed.
                                If the specified `section’ does not exist, returns False.
**has_section**(section)-   Indicate whether the named section is present in the configuration.
**items**(section=<object object>, raw=False, vars=None)      Return a list of (name, value) tuples for each option in a section.
**options**(section) -       Return a list of option names for the given section name.
**popitem()** -              Remove a section from the parser and return it as a (section_name, section_proxy) tuple. I
**read(**filenames, encoding=None) -   Read and parse a filename or an iterable of filenames.
**read_dict**(dictionary, source='<dict>') -     Read configuration from a dictionary.
**read_file**(f, source=None) -                 Like read() but the argument must be a file-like object.
**read_string**(string, source='<string>') -         Read configuration from a given string.
**remove_option**(section, option) -       Remove an option.
**remove_section**(section) -            Remove a file section.
**sections()** -                         Return a list of section names, excluding DEFAULT]
**set**(section, option, value=None) -   Set an option.
**write**(fp, space_around_delimiters=True) -     Write an .ini-format representation of the configuration state.


