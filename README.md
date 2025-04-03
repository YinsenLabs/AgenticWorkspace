# AgenticWorkspace

A workspace agent module integrate various functionalities to enhance productivity and efficiency in managing tasks and interactions.

## Features

- Automate create google calendar event

## Project Structure

```
AgenticWorkspace/
├── agentic_workspace/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── calendar_event.py
│   ├── llm_clients/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── gemini_calls.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_calendar_event.py
│   └── test_gemini_calls.py
├── notebooks/
│   └── calendar_event_example.ipynb
├── README.md
├── requirements.txt
└── setup.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Pydantic team for their excellent work
- Inspired by various LLM output parsing needs in production environments

## Contact

QuyThanh - tothanh1feb3.quinn@gmail.com

Project Link: [https://github.com/YinsenLabs/AgenticWorkspace](https://github.com/YinsenLabs/AgenticWorkspace)
