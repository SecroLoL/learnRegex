
<h3>Anchors</h3>

^   Start of string, or start of line in multi-line pattern<br>
\A   Start of string
$   End of string, or end of line in multi-line pattern
\Z  End of string
\b  Word boundary
\B  Not word boundary
\<  Start of word
\>  End of word


<h3>Character Classes</h3>
\c  Control character
\s  White space
\S  Not white space
\d  Digit
\D  Not digit
\w  Word
\W  Not word
\x  Hexade­cimal digit
\O  Octal digit


<h3>Quanti­fiers</h3>
*   0 or more
{3} Exactly 3
+   1 or more
{3,}    3 or more
?   0 or 1
{3,5}   3, 4 or 5


	
<h3>Groups and Ranges</h3>
.   Any character except new line (\n)
(a|b)   a or b
(...)   Group
(?:...) Passive (non-c­apt­uring) group
[abc]   Range (a or b or c)
[^abc]  Not (a or b or c)
[a-q]   Lower case letter from a to q
[A-Q]   Upper case letter from A to Q
[0-7]   Digit from 0 to 7
\x  Group/­sub­pattern number "­x"
Ranges are inclusive.


<h3>Escape Sequences</h3>
\   Escape following character
\Q  Begin literal sequence
\E  End literal sequence
"­Esc­api­ng" is a way of treating characters which have a special meaning in regular expres­sions literally, rather than as special charac­ters.


<h3>Common Metach­ara­cters</h3>
^  [  .  $  {  *  (
\  +  )  |  ?  <  >
The escape character is usually \
