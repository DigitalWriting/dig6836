Here are ten practice problems for generating regular expressions using Python, along with their solution code:

**1. Problem:** Write a regular expression that matches any sequence of digits from 0 to 9.

**Solution:**
```python
import re

pattern = r"\d+"
```

**2. Problem:** Write a regular expression that matches a valid email address.

**Solution:**
```python
import re

pattern = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
```

**3. Problem:** Write a regular expression that matches a phone number in the format "XXX-XXX-XXXX", where X represents a digit.

**Solution:**
```python
import re

pattern = r"\d{3}-\d{3}-\d{4}"
```

**4. Problem:** Write a regular expression that matches a URL starting with either "http://" or "https://".

**Solution:**
```python
import re

pattern = r"https?://\w+(\.\w+)+"
```

**5. Problem:** Write a regular expression that matches a string containing only lowercase letters.

**Solution:**
```python
import re

pattern = r"^[a-z]+$"
```

**6. Problem:** Write a regular expression that matches a string containing at least one uppercase letter and one lowercase letter.

**Solution:**
```python
import re

pattern = r"(?=.*[a-z])(?=.*[A-Z]).+"
```

**7. Problem:** Write a regular expression that matches a string containing a word starting with "cat".

**Solution:**
```python
import re

pattern = r"\bcat\w*\b"
```

**8. Problem:** Write a regular expression that matches a hexadecimal color code in the format "#RRGGBB".

**Solution:**
```python
import re

pattern = r"#[0-9a-fA-F]{6}"
```

**9. Problem:** Write a regular expression that matches a date in the format "MM/DD/YYYY".

**Solution:**
```python
import re

pattern = r"\d{2}/\d{2}/\d{4}"
```

**10. Problem:** Write a regular expression that matches a string containing three consecutive identical characters.

**Solution:**
```python
import re

pattern = r"(.)\1\1"
```

These practice problems and solutions cover a range of different regular expression patterns and can help you get familiar with generating regular expressions using Python.
