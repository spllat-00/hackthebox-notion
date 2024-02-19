writeup_template = [
    { # H1 TOC
        "type": "heading_1",
        "heading_1": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": "🔖 Table of Contents"
                }
            }],
            "color": "default",
            "is_toggleable": False
        }
    },
    { # TOC
        "type": "table_of_contents",
        "table_of_contents": {
            "color": "default"
        }
    },
    { # Divider
        "type": "divider",
        "divider": {}
    },
    { # H1 Requirements
        "type": "heading_1",
        "heading_1": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": "📖 Requirements"
                }
            }],
            "color": "default",
            "is_toggleable": False
        }
    },
    { # H2 Toggle IP
        "type": "heading_2",
        "heading_2": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": "IP"
                }
            }],
            "color": "default",
            "is_toggleable": True,
            "children": [{
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": "IP_here"
                        }
                    }]
                }
            }]
        }
    },
    { # H2 Toggle DNS
        "type": "heading_2",
        "heading_2": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": "DNS"
                }
            }],
            "color": "default",
            "is_toggleable": True,
            "children": [{
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": "DNS_here"
                        }
                    }]
                }
            }]
        }
    },
    { # Empty Block
        "type": "paragraph",
        "paragraph": {
            "rich_text": []
        }
    },
    { # Para Image Card
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": "Image Card of Machine Pwned"
                }
            }]
        }
    },
    { # Divider
        "type": "divider",
        "divider": {}
    },
    { # H1 Recon
        "type": "heading_1",
        "heading_1": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": "🔍 Recon"
                }
            }],
            "color": "default",
            "is_toggleable": False
        }
    },
    { # H2 nms
        "type": "heading_2",
        "heading_2": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": "nms"
                }
            }],
            "color": "default",
            "is_toggleable": False
        }
    },
    { # Code nms
        "type": "code",
        "code": {
            "caption": [
                {
                    "href": "https://github.com/spllat-00/Shelloox",
                    "plain_text": "Shelloox nmap Scanner",
                    "text": {
                        "content": "Shelloox nmap Scanner",
                        "link": {
                            "url": "https://github.com/spllat-00/Shelloox"
                        }
                    },
                },
            ],
            "rich_text": [{
                "type":"text",
                "text":{
                    "content": "nms -u <IP>"
                }
            }],
            "language": "bash"
        }
    },
    { # Empty Block
        "type": "paragraph",
        "paragraph": {
            "rich_text": []
        }
    },
    { # Quote
        "type": "quote",
        "quote": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": "Additional reconnaissance here"
                }
            }]
        }
    },
    { # Empty Block
        "type": "paragraph",
        "paragraph": {
            "rich_text": []
        }
    },
    { # Divider
        "type": "divider",
        "divider": {}
    },
    { # H1 Foothold
        "type": "heading_1",
        "heading_1": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": "🪤 Foothold"
                }
            }],
            "color": "default",
            "is_toggleable": False
        }
    },
    { # Empty Block
        "type": "paragraph",
        "paragraph": {
            "rich_text": []
        }
    },
    { # Para Foothold Steps
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": "... Foothold Steps"
                }
            }]
        }
    },
    { # Empty Block
        "type": "paragraph",
        "paragraph": {
            "rich_text": []
        }
    },
    { # Divider
        "type": "divider",
        "divider": {}
    },
    { # H1 Priv Esc
        "type": "heading_1",
        "heading_1": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": "📖 Priv Esc"
                }
            }],
            "color": "default",
            "is_toggleable": False
        }
    },
    { # Empty Block
        "type": "paragraph",
        "paragraph": {
            "rich_text": []
        }
    },
    { # Para Priv Esc Steps
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": "... Priv Esc Steps"
                }
            }]
        }
    },
    { # Empty Block
        "type": "paragraph",
        "paragraph": {
            "rich_text": []
        }
    },
    { # Divider
        "type": "divider",
        "divider": {}
    },
    { # H1 Flags
        "type": "heading_1",
        "heading_1": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": "🏁 Flags"
                }
            }],
            "color": "default",
            "is_toggleable": False
        }
    },
    { # H2 Toggle User Flag
        "type": "heading_2",
        "heading_2": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": "User Flag"
                }
            }],
            "color": "default",
            "is_toggleable": True,
            "children": [{
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": "32-bit Flag"
                        }
                    }]
                }
            }]
        }
    },
    { # H2 Toggle Root Flag
        "type": "heading_2",
        "heading_2": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": "Root Flag"
                }
            }],
            "color": "default",
            "is_toggleable": True,
            "children": [{
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": "32-bit Flag"
                        }
                    }]
                }
            }]
        }
    },
    { # Divider
        "type": "divider",
        "divider": {}
    },
]