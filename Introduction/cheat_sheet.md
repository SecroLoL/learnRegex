
<h3>Anchors</h3>

^   Start of string, or start of line in multi-line pattern<br>
\A   Start of string<br>
$   End of string, or end of line in multi-line pattern<br>
\Z  End of string<br>
\b  Word boundary<br>
\B  Not word boundary<br>
\<  Start of word<br>
\>  End of word


<h3>Character Classes</h3>
\c  Control character<br>
\s  White space<br>
\S  Not white space<br>
\d  Digit<br>
\D  Not digit<br>
\w  Word<br>
\W  Not word<br>
\x  Hexade­cimal digit<br>
\O  Octal digit


<h3>Quanti­fiers</h3>
*   0 or more<br>
{3} Exactly 3<br>
+   1 or more<br>
{3,}    3 or more<br>
?   0 or 1<br>
{3,5}   3, 4 or 5


	
<h3>Groups and Ranges</h3>
.   Any character except new line (\n)<br>
(a|b)   a or b<br>
(...)   Group<br>
(?:...) Passive (non-c­apt­uring) group<br>
[abc]   Range (a or b or c)<br>
[^abc]  Not (a or b or c)<br>
[a-q]   Lower case letter from a to q<br>
[A-Q]   Upper case letter from A to Q<br>
[0-7]   Digit from 0 to 7<br>
\x  Group/­sub­pattern number "­x"<br>
Ranges are inclusive.


<h3>Escape Sequences</h3>
\   Escape following character<br>
\Q  Begin literal sequence<br>
\E  End literal sequence<br>
"­Esc­api­ng" is a way of treating characters which have a special meaning in regular expres­sions literally, rather than as special charac­ters.


<h3>Common Metach­ara­cters</h3>
^  [  .  $  {  *  (<br>
\  +  )  |  ?  <  ><br>
The escape character is usually \
