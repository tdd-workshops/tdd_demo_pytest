# TDD Demo with Pytest

You are given strings of different lengths. If the number of vowels are more than 30% of the string length then insert ‘mummy’ for each continuous set of vowels.

## Rules

- ✅  h**i**s → h**mummy**s
- ✅  h**ea**r → h**mummy**r 
- ❌  h**ea**r → h**mummymummy**r


## Sample Input

```
“” → “” 				    // empty string
“str” → “str” 			    // no vowels
“a” → “mummy” 		        // single vowel
“blah” → “blah” 		    // < 30% length
“bla” → “blmummy” 		    // > 30% length
“blaa” → “blmummy” 	        // continuous vowels
“blaaha” → “blmummyhmummy” 	// multi sets of vowels
“blA” → “blmummy” 	        // capital letters
```

## To run the test

```bash
pytest
```
