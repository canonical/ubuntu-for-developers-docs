(use-python)=
# Develop with Python on Ubuntu

This tutorial shows how to run, check, and debug Python scripts on Ubuntu. For instructions on how to install Python and related tooling, including IDEs, debuggers, and linters, see the dedicated guide on {ref}`install-python`. This article assumes that tooling suggested in that article has been installed.

:::{important}
To separate the system installation of Python from your development and testing setup, only use virtual environments for installing development project dependencies and running the developed code. This guide uses the standard `venv` virtual environment.
:::


## Preparing a Python virtual environment

0. (Optional) Create a directory for Python development, as well as a directory for the new project:

    ```none
    $ mkdir -p ~/python/helloworld
    $ cd ~/python/helloworld
    ```

1. Create a separate virtual environment for the new project (specifying `.venv` as the directory for it):

    ```none
    $ python3 -m venv .venv
    ```

2. Activate the virtual environment by sourcing the `activate` script:

    ```none
    $ source .venv/bin/activate
    ```

3. Check that the environment has been set up:

    ```{terminal}
    :dir: ~/python/helloworld
    :user: dev
    :host: ubuntu
    :input: which python3

    /home/dev/python/helloworld/.venv/bin/python3
    ```

::::{note}
If you attempt to install a Python package using `pip` outside of a Python virtual environment, such as `venv`, on an Ubuntu (Debian) system, you will receive a warning that explains that you should keep the system installation of Python (installed using `.deb` packages from Ubuntu repositories) separate from Python packages installed using `pip`:

:::{raw} html
<div class="highlight-default notranslate"><div class="highlight"><pre>
$ which pip
/usr/bin/pip

$ pip install -r requirements.txt
<span style="font-weight:bold;"><span style="color:red">error:</span> externally-managed-environment</span>

<span style="color:red;">×</span> This environment is externally managed
<span style="color:red;">╰─></span> To install Python packages system-wide, try apt install
python3-xyz, where xyz is the package you are trying to
install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.12/README.venv for more information.

<span style="font-weight:bold;color:magenta;">note</span>: If you believe this is a mistake, please contact your Python
installation or OS distribution provider. You can override this,
at the risk of breaking your Python installation or OS, by passing
--break-system-packages.
<span style="font-weight:bold;color:cyan;">hint</span>: See PEP 668 for the detailed specification.
</pre></div></div>
:::
::::


(creating-a-basic-python-program)=
## Creating a basic Python program

To illustrate the installation of a dependency confined to the Python virtual environment, the following example uses the `requests` library for handling HTTP requests.

1. Create a `requirements.txt` file with the list of dependencies. For example:

    ```none
    $ echo "requests" > requirements.txt
    ```

2. Install the dependencies:

    ```none
    $ pip install -r requirements.txt
    ```

   Checking the list of Python packages installed within the virtual environment should show output similar to this:

    ```{terminal}
    :dir: ~/python/helloworld
    :user: dev
    :host: ubuntu
    :input: pip list

    Package  Version
    -------- -------
    certifi            2025.1.31
    charset-normalizer 3.4.1
    idna               3.10
    pip                24.2
    requests           2.32.3
    urllib3            2.4.0
    ```

    (The version numbers can differ based on your environment.)

3. Write a Python script that uses the installed dependency. For example, create a {file}`helloworld.py` file with the following contents:

    ```{code-block} python
    :caption: `helloworld.py`

    import requests


    def hello_world():
        # Use the example HTTP response service
        url = "https://httpbin.org/post"

        # Define a custom header for the POST method
        header = {"Message": "Hello, world!"}

        try:
            # Send the defined header to the response service
            response = requests.post(url, headers=header)

            # Basic error handling
            response.raise_for_status()

            # Parse the response
            response_data = response.json()

            # Print the message
            print(response_data["headers"]["Message"])

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")


    if __name__ == "__main__":
        hello_world()
    ```

4. Executing the program should result in the message you defined and sent using the `POST` method printed to standard output:

    ```{terminal}
    :dir: ~/python/helloworld
    :user: dev
    :host: ubuntu
    :input: python3 helloworld.py

    Hello, world!
    ```

## Improving Python code with the help of tooling

Use linters and formatters to improve the quality and style of your Python code to achieve consistency and better readability.

In this example, we use the [Flake8](https://flake8.pycqa.org/) code checker and [Black](https://github.com/psf/black) formatter to identify areas for improvement and automatically format code. See {ref}`install-python` for instructions on how to install these tools.


### Checking Python code with Flake8

Consider the 'Hello, world!' script shown in {ref}`creating-a-basic-python-program`. Let's introduce a simple style transgression into the code by deleting one of the blank lines after the `hello_world()` function:

```{code-block} python
    :caption: `helloworld.py`
    :linenos:

import requests


def hello_world():
    # Use the example HTTP response service
    url = "https://httpbin.org/post"

    # Define a custom header for the POST method
    header = {"Message": "Hello, world!"}

    try:
        # Send the defined header to the response service
        response = requests.post(url, headers=header)

        # Basic error handling
        response.raise_for_status()

        # Parse the response
        response_data = response.json()

        # Print the message
        print(response_data["headers"]["Message"])

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    hello_world()
```

Running the Flake8 checker identifies the offense and informs us that it expects one more blank line on line number 27:

:::{raw} html
<div class="highlight-default notranslate"><div class="highlight"><pre>$ flake8 helloworld.py
<span style="font-weight:bold;">helloworld.py</span><span style="color:teal;">:</span>27<span style="color:teal;">:</span>1<span style="color:teal;">:</span> <span style="font-weight:bold;"></span><span style="font-weight:bold;color:red;">E305</span> expected 2 blank lines after class
                    or function definition, found 1</pre></div></div>
:::


### Reformatting Python code with Black

Running the Black formatter automatically reformats the code and fixes the problem:

:::{raw} html
<div class="highlight-default notranslate"><div class="highlight"><pre>$ black helloworld.py
<span style="font-weight:bold;">reformatted helloworld.py</span>

<span style="font-weight:bold;">All done!</span> ✨ 🍰 ✨
<span style="font-weight:bold;"><span style="color:blue;">1 file</span> reformatted.</pre></div></div>
:::

:::{admonition} Black is opinionated
Note that Black proceeds to reformat the code without asking for a confirmation.
:::


## Debugging Python code

To allow for the possibility of inspecting the state of the script at different points of execution, add breakpoints. In this example, we use the `ipdb` debugger, which is an enhanced version of the built-in `pdb` debugger.

1. Add `ipdb` to the list of dependencies:

    ```none
    $ echo "ipdb" >> requirements.txt
    ```

2. Install the dependencies:

    ```none
    $ pip install -r requirements.txt
    ```

3. Add `ipdb` module import, and insert a breakpoint in the code (see line 23):

    ```{code-block} python
    :caption: `helloworld.py`
    :linenos:

    import requests
    import ipdb


    def hello_world():
        # Use the example HTTP response service
        url = "https://httpbin.org/post"

        # Define a custom header for the POST method
        header = {"Message": "Hello, world!"}

        try:
            # Send the defined header to the response service
            response = requests.post(url, headers=header)

            # Basic error handling
            response.raise_for_status()

            # Parse the response
            response_data = response.json()

            # Set a breakpoint to check response data
            ipdb.set_trace()

            # Print the message
            print(response_data["headers"]["Message"])

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

    if __name__ == "__main__":
        hello_world()
    ```

4. Execute the script to interact with the `ipdb` debugger:

    :::{raw} html
    <div class="highlight-default notranslate"><div class="highlight"><pre>$ python3 helloworld.py

    &gt; <span style="color:green">/home/rkratky/python/hw.py</span>(<span style="color:#52FF52">26</span>)<span style="color:teal">hello_world</span><span style="color:blue">()</span>
        <span style="color:green">25</span>         <span style="font-style:italic;color:grey"># Print the message</span>
    <span style="color:green">---&gt; 26</span>         print(response_data[<span style="color:brown">"headers"</span>][<span style="color:brown">"Message"</span>])
        <span style="color:green">27</span>

    ipdb&gt;
    ipdb&gt; pp response_data['headers']
    {'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Length': '0',
    'Host': 'httpbin.org',
    'Message': 'Hello, world!',
    'User-Agent': 'python-requests/2.32.3',
    'X-Amzn-Trace-Id': 'Root=1-680a5186-49625c625bc31933473464b7'}
    ipdb&gt; response_data['headers']['Message']
    'Hello, world!'</pre></div></div>
    :::

    In the above example, we query the `response_data` variable using the `pp` (pretty print) command and then by specifying the `Message` header directly.


## Testing Python code with a unit test

The following example shows how to use the `pytest` testing tool. First we implement a simple unit test that supplies mock data in place of querying the remote service and compares the output with the expected return value from the `hello_world()` function. Then we run `pytest` to perform the test.

1. Create a unit-test file, {file}`helloworld_test.py`, with the following contents:

    ```{code-block} python
        :caption: `helloworld_test.py`

    from helloworld import hello_world

    MOCK_RESPONSE_DATA = {"headers": {"Message": "Hello, world!"}}

    class MockResponse:
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

        def raise_for_status(self):
            pass


    def test_hello_world(mocker, capsys):
        # Mock the requests.post method
        mocker.patch("requests.post", return_value=MockResponse(MOCK_RESPONSE_DATA))

        # Call the function to be tested
        hello_world()

        # Get the printed output
        captured = capsys.readouterr()

        # Check that the output is as expected
        assert captured.out.strip() == "Hello, world!"
    ```

2. Run the unit test using `pytest`:

    :::{raw} html
    <div class="highlight-default notranslate"><div class="highlight"><pre>$ pytest helloworld_test.py
    <span style="font-weight:bold;">================= test session starts =====================</span>
    platform linux -- Python 3.12.7, pytest-8.3.2, pluggy-1.5.0
    rootdir: /home/user/python
    plugins: cov-5.0.0, xdist-3.6.1, mock-3.14.0,
             requests_mock-1.12.1, typeguard-4.3.0
    <span style="font-weight:bold;">collected 1 item</span>

    helloworld_test.py <span style="color:green">.                                 [100%]</span>

    <span style="color:green">====================</span> <span style="color:#52FF52">1 passed</span> <span style="color:green">in 0.01s ====================</span></pre></div></div>
    :::
