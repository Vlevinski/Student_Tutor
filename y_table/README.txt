# Pretty table module
Help on class PrettyTable in module prettytable:

class PrettyTable(builtins.object)
 |  PrettyTable(field_names=None, **kwargs)
 |  
 |  Methods defined here:
 |  
 |  __getattr__(self, name)
 |  
 |  __getitem__(self, index)
 |  
 |  __init__(self, field_names=None, **kwargs)
 |      Return a new PrettyTable instance
 |  
 |      Arguments:
 |  
 |      encoding - Unicode encoding scheme used to decode any encoded input
 |      field_names - list or tuple of field names
 |      fields - list or tuple of field names to include in displays
 |      start - index of first data row to include in output
 |      end - index of last data row to include in output PLUS ONE (list slice style)
 |      header - print a header showing field names (True or False)
 |      header_style - stylisation to apply to field names in header ("cap", "title", "upper", "lower" or None)
 |      border - print a border around the table (True or False)
 |      hrules - controls printing of horizontal rules after rows.  Allowed values: FRAME, HEADER, ALL, NONE
 |      vrules - controls printing of vertical rules between columns.  Allowed values: FRAME, ALL, NONE
 |      int_format - controls formatting of integer data
 |      float_format - controls formatting of floating point data
 |      padding_width - number of spaces on either side of column data (only used if left and right paddings are None)
 |      left_padding_width - number of spaces on left hand side of column data
 |      right_padding_width - number of spaces on right hand side of column data
 |      vertical_char - single character string used to draw vertical lines
 |      horizontal_char - single character string used to draw horizontal lines
 |      junction_char - single character string used to draw line junctions
 |      sortby - name of field to sort rows by
 |      sort_key - sorting key function, applied to data points before sorting
 |      valign - default valign for each row (None, "t", "m" or "b")
 |      reversesort - True or False to sort in descending or ascending order
 |  
 |  __str__(self)
 |      Return str(self).
 |  
 |  __unicode__(self)
 |  
 |  add_column(self, fieldname, column, align='c', valign='t')
 |      Add a column to the table.
 |  
 |      Arguments:
 |  
 |      fieldname - name of the field to contain the new column of data
 |      column - column of data, should be a list with as many elements as the
 |      table has rows
 |      align - desired alignment for this column - "l" for left, "c" for centre and "r" for right
 |      valign - desired vertical alignment for new columns - "t" for top, "m" for middle and "b" for bottom
 |  
 |  add_row(self, row)
 |      Add a row to the table
 |  
 |      Arguments:
 |  
 |      row - row of data, should be a list with as many elements as the table
 |      has fields
 |  
 |  clear(self)
 |      Delete all rows and field names from the table, maintaining nothing but styling options
 |  
 |  clear_rows(self)
 |      Delete all rows from the table but keep the current field names
 |  
 |  copy(self)
 |  
 |  del_row(self, row_index)
 |      Delete a row to the table
 |  
 |      Arguments:
 |  
 |      row_index - The index of the row you want to delete.  Indexing starts at 0.
 |  
 |  get_html_string(self, **kwargs)
 |      Return string representation of HTML formatted version of table in current state.
 |  
 |      Arguments:
 |  
 |      start - index of first data row to include in output
 |      end - index of last data row to include in output PLUS ONE (list slice style)
 |      fields - names of fields (columns) to include
 |      header - print a header showing field names (True or False)
 |      border - print a border around the table (True or False)
 |      hrules - controls printing of horizontal rules after rows.  Allowed values: ALL, FRAME, HEADER, NONE
 |      vrules - controls printing of vertical rules between columns.  Allowed values: FRAME, ALL, NONE
 |      int_format - controls formatting of integer data
 |      float_format - controls formatting of floating point data
 |      padding_width - number of spaces on either side of column data (only used if left and right paddings are None)
 |      left_padding_width - number of spaces on left hand side of column data
 |      right_padding_width - number of spaces on right hand side of column data
 |      sortby - name of field to sort rows by
 |      sort_key - sorting key function, applied to data points before sorting
 |      attributes - dictionary of name/value pairs to include as HTML attributes in the <table> tag
 |      xhtml - print <br/> tags if True, <br> tags if false
 |  
 |  get_string(self, **kwargs)
 |      Return string representation of table in current state.
 |  
 |      Arguments:
 |  
 |      start - index of first data row to include in output
 |      end - index of last data row to include in output PLUS ONE (list slice style)
 |      fields - names of fields (columns) to include
 |      header - print a header showing field names (True or False)
 |      border - print a border around the table (True or False)
 |      hrules - controls printing of horizontal rules after rows.  Allowed values: ALL, FRAME, HEADER, NONE
 |      vrules - controls printing of vertical rules between columns.  Allowed values: FRAME, ALL, NONE
 |      int_format - controls formatting of integer data
 |      float_format - controls formatting of floating point data
 |      padding_width - number of spaces on either side of column data (only used if left and right paddings are None)
 |      left_padding_width - number of spaces on left hand side of column data
 |      right_padding_width - number of spaces on right hand side of column data
 |      vertical_char - single character string used to draw vertical lines
 |      horizontal_char - single character string used to draw horizontal lines
 |      junction_char - single character string used to draw line junctions
 |      sortby - name of field to sort rows by
 |      sort_key - sorting key function, applied to data points before sorting
 |      reversesort - True or False to sort in descending or ascending order
 |      print empty - if True, stringify just the header for an empty table, if False return an empty string
 |  
 |  set_style(self, style)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  align
 |  
 |  attributes
 |      A dictionary of HTML attribute name/value pairs to be included in the <table> tag when printing HTML
 |  
 |      Arguments:
 |  
 |      attributes - dictionary of attributes
 |  
 |  border
 |      Controls printing of border around table
 |  
 |      Arguments:
 |  
 |      border - print a border around the table (True or False)
 |  
 |  end
 |      End index of the range of rows to print
 |  
 |      Arguments:
 |  
 |      end - index of last data row to include in output PLUS ONE (list slice style)
 |  
 |  fields
 |      List or tuple of field names to include in displays
 |  
 |      Arguments:
 |  
 |      fields - list or tuple of field names to include in displays
 |  
 |  float_format
 |      Controls formatting of floating point data
 |      Arguments:
 |  
 |      float_format - floating point format string
 |  
 |  format
 |      Controls whether or not HTML tables are formatted to match styling options
 |  
 |      Arguments:
 |  
 |      format - True or False
 |  
 |  header
 |      Controls printing of table header with field names
 |  
 |      Arguments:
 |  
 |      header - print a header showing field names (True or False)
 |  
 |  header_style
 |      Controls stylisation applied to field names in header
 |  
 |      Arguments:
 |  
 |      header_style - stylisation to apply to field names in header ("cap", "title", "upper", "lower" or None)
 |  
 |  horizontal_char
 |      The charcter used when printing table borders to draw horizontal lines
 |  
 |      Arguments:
 |  
 |      horizontal_char - single character string used to draw horizontal lines
 |  
 |  hrules
 |      Controls printing of horizontal rules after rows
 |  
 |      Arguments:
 |  
 |      hrules - horizontal rules style.  Allowed values: FRAME, ALL, HEADER, NONE
 |  
 |  int_format
 |      Controls formatting of integer data
 |      Arguments:
 |  
 |      int_format - integer format string
 |  
 |  junction_char
 |      The charcter used when printing table borders to draw line junctions
 |  
 |      Arguments:
 |  
 |      junction_char - single character string used to draw line junctions
 |  
 |  left_padding_width
 |      The number of empty spaces between a column's left edge and its content
 |  
 |      Arguments:
 |  
 |      left_padding - number of spaces, must be a positive integer
 |  
 |  max_width
 |  
 |  padding_width
 |      The number of empty spaces between a column's edge and its content
 |  
 |      Arguments:
 |  
 |      padding_width - number of spaces, must be a positive integer
 |  
 |  print_empty
 |      Controls whether or not empty tables produce a header and frame or just an empty string
 |  
 |      Arguments:
 |  
 |      print_empty - True or False
 |  
 |  reversesort
 |      Controls direction of sorting (ascending vs descending)
 |  
 |      Arguments:
 |  
 |      reveresort - set to True to sort by descending order, or False to sort by ascending order
 |  
 |  right_padding_width
 |      The number of empty spaces between a column's right edge and its content
 |  
 |      Arguments:
 |  
 |      right_padding - number of spaces, must be a positive integer
 |  
 |  sort_key
 |      Sorting key function, applied to data points before sorting
 |  
 |      Arguments:
 |  
 |      sort_key - a function which takes one argument and returns something to be sorted
 |  
 |  sortby
 |      Name of field by which to sort rows
 |  
 |      Arguments:
 |  
 |      sortby - field name to sort by
 |  
 |  start
 |      Start index of the range of rows to print
 |  
 |      Arguments:
 |  
 |      start - index of first data row to include in output
 |  
 |  valign
 |  
 |  vertical_char
 |      The charcter used when printing table borders to draw vertical lines
 |  
 |      Arguments:
 |  
 |      vertical_char - single character string used to draw vertical lines
 |  
 |  vrules
 |      Controls printing of vertical rules between columns
 |  
 |      Arguments:
 |  
 |      vrules - vertical rules style.  Allowed values: FRAME, ALL, NONE
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  field_names = ['City name', 'Area', 'Population', 'Annual Rainfall']

None

Process finished with exit code 0
