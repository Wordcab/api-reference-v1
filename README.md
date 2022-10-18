# Wordcab API

**Summarize any business communications at scale with Wordcab's API.** 

**Wordcab** is a summarization service that provides a simple API to summarize any `audio`, `text`, or `JSON` file.  

It includes also compatibility with popular transcripts platforms like [AssemblyAI](https://www.assemblyai.com/), 
[Deepgram](https://deepgram.com/), [Rev.ai](https://www.rev.ai/), [Otter.ai](https://otter.ai/) or 
[Sonix.ai](https://sonix.ai/).

## Getting Started

You can learn more about Wordcab services and pricing on [our website](https://wordcab.com/).

If you want to try out the API, you can [signup](https://wordcab.com/signup/) for a free account and start using the API
right away.

Discover the [API documentation](https://docs.wordcab.com/reference/getting-started-with-your-api) and play with the 
different endpoints.

## Contact

If you have any questions, please contact us at [info@wordcab.com](mailto:info@wordcab.com).

## Python example

```bash
# Activate your python environment
$ pip install python-dotenv
```

Be sure to include your Wordcab API key in a `.env` file in the same directory as your script.  
You can find your API key in your [Wordcab dashboard](https://wordcab.com/dashboard/).

Your `.env` file should look like this:

```bash
WORDCAB_API_KEY=YOUR_API_KEY
```

Launch the python example script:

```bash
$ python test/test_api.py
```
