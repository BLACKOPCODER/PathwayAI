import json

class RoadmapGenerator:
    def __init__(self):
        self.roadmap_templates = {
            "Web Development": {
                "beginner": [
                    {
                        "title": "HTML Fundamentals",
                        "description": "Learn the basics of HTML including tags, elements, attributes, and document structure. Understand semantic HTML and best practices.",
                        "estimated_duration": "1-2 weeks",
                        "resources": ["MDN Web Docs", "W3Schools", "freeCodeCamp"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=UB1O30fR-EE",
                            "https://www.youtube.com/watch?v=pQN-pnXPaVg"
                        ]
                    },
                    {
                        "title": "CSS Basics & Styling",
                        "description": "Master CSS selectors, properties, box model, flexbox, and grid. Learn responsive design principles and mobile-first approach.",
                        "estimated_duration": "2-3 weeks",
                        "resources": ["CSS Tricks", "Flexbox Froggy", "Grid Garden"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=1Rs2ND1ryYc",
                            "https://www.youtube.com/watch?v=yfoY53QXEnI"
                        ]
                    },
                    {
                        "title": "JavaScript Fundamentals",
                        "description": "Learn JavaScript basics: variables, data types, functions, loops, and conditionals. Understand DOM manipulation and events.",
                        "estimated_duration": "3-4 weeks",
                        "resources": ["JavaScript.info", "Eloquent JavaScript", "MDN"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=W6NZfCO5SIk",
                            "https://www.youtube.com/watch?v=hdI2bqOjy3c"
                        ]
                    },
                    {
                        "title": "Git & Version Control",
                        "description": "Learn Git basics, GitHub, branches, commits, pull requests, and collaboration workflows.",
                        "estimated_duration": "1 week",
                        "resources": ["Git Documentation", "GitHub Learning Lab"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=RGOj5yH7evk",
                            "https://www.youtube.com/watch?v=USjZcfj8yxE"
                        ]
                    },
                    {
                        "title": "Build Your First Website",
                        "description": "Create a complete portfolio website using HTML, CSS, and JavaScript. Deploy it using GitHub Pages or Netlify.",
                        "estimated_duration": "2 weeks",
                        "resources": ["GitHub Pages", "Netlify"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=OXGznpKZ_sA",
                            "https://www.youtube.com/watch?v=mJpNZ6x_r7A"
                        ]
                    }
                ],
                "intermediate": [
                    {
                        "title": "Advanced JavaScript & ES6+",
                        "description": "Master modern JavaScript: arrow functions, promises, async/await, modules, destructuring, spread operator.",
                        "estimated_duration": "3 weeks",
                        "resources": ["ES6 Features", "JavaScript.info"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=NCwa_xi0Uuc",
                            "https://www.youtube.com/watch?v=IjjSvkrSPXg"
                        ]
                    },
                    {
                        "title": "React Fundamentals",
                        "description": "Learn React components, props, state, hooks, and component lifecycle. Build interactive UIs.",
                        "estimated_duration": "4 weeks",
                        "resources": ["React Documentation", "React Tutorial"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=bMknfKXIFA8",
                            "https://www.youtube.com/watch?v=w7ejDZ8SWv8"
                        ]
                    },
                    {
                        "title": "Backend with Node.js",
                        "description": "Learn Node.js, Express.js, RESTful APIs, middleware, and server-side JavaScript.",
                        "estimated_duration": "3 weeks",
                        "resources": ["Node.js Documentation", "Express.js Guide"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=Oe421EPjeBE",
                            "https://www.youtube.com/watch?v=fBNz5xF-Kx4"
                        ]
                    },
                    {
                        "title": "Database Integration",
                        "description": "Learn MongoDB or PostgreSQL, database design, CRUD operations, and ORM/ODM tools.",
                        "estimated_duration": "2 weeks",
                        "resources": ["MongoDB University", "PostgreSQL Tutorial"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=-56x56UppqQ",
                            "https://www.youtube.com/watch?v=qw--VYLpxG4"
                        ]
                    },
                    {
                        "title": "Full-Stack Project",
                        "description": "Build a complete MERN/PERN stack application with authentication, CRUD operations, and deployment.",
                        "estimated_duration": "4 weeks",
                        "resources": ["Project Ideas", "Deployment Guides"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=98BzS5Oz5E4",
                            "https://www.youtube.com/watch?v=mrHNSanmqQ4"
                        ]
                    }
                ],
                "advanced": [
                    {
                        "title": "Advanced React Patterns",
                        "description": "Master React hooks, context API, custom hooks, performance optimization, and state management with Redux/Zustand.",
                        "estimated_duration": "3 weeks",
                        "resources": ["React Patterns", "Redux Documentation"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=3XaXKiXtNjw",
                            "https://www.youtube.com/watch?v=poQXNp9ItL4"
                        ]
                    },
                    {
                        "title": "TypeScript",
                        "description": "Learn TypeScript for type-safe JavaScript, interfaces, generics, and integration with React.",
                        "estimated_duration": "2 weeks",
                        "resources": ["TypeScript Handbook", "TypeScript Deep Dive"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=BwuLxPH8IDs",
                            "https://www.youtube.com/watch?v=30LWjhZzg50"
                        ]
                    },
                    {
                        "title": "Testing & CI/CD",
                        "description": "Learn Jest, React Testing Library, E2E testing with Cypress, and CI/CD pipelines.",
                        "estimated_duration": "2 weeks",
                        "resources": ["Testing Library Docs", "GitHub Actions"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=8Xwq35cPwYg",
                            "https://www.youtube.com/watch?v=scEDHsr3APg"
                        ]
                    },
                    {
                        "title": "Microservices Architecture",
                        "description": "Learn microservices design, Docker, Kubernetes, and scalable application architecture.",
                        "estimated_duration": "4 weeks",
                        "resources": ["Docker Documentation", "Kubernetes Tutorial"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=pTFZFxd4hOI",
                            "https://www.youtube.com/watch?v=X48VuDVv0do"
                        ]
                    },
                    {
                        "title": "Production & DevOps",
                        "description": "Master deployment, monitoring, logging, security best practices, and cloud platforms (AWS/Azure/GCP).",
                        "estimated_duration": "3 weeks",
                        "resources": ["AWS Documentation", "DevOps Roadmap"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=3c-iBn73dDE",
                            "https://www.youtube.com/watch?v=j5Zsa_eOXeY"
                        ]
                    }
                ]
            },
            "Data Science": {
                "beginner": [
                    {
                        "title": "Python Programming Basics",
                        "description": "Learn Python fundamentals: variables, data types, control structures, functions, and basic OOP concepts.",
                        "estimated_duration": "2-3 weeks",
                        "resources": ["Python.org", "Real Python", "Python for Everybody"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=rfscVS0vtbw",
                            "https://www.youtube.com/watch?v=_uQrJ0TkZlc"
                        ]
                    },
                    {
                        "title": "NumPy & Pandas",
                        "description": "Master data manipulation with NumPy arrays and Pandas DataFrames. Learn data cleaning and preprocessing.",
                        "estimated_duration": "2 weeks",
                        "resources": ["NumPy Documentation", "Pandas Documentation"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=QUT1VHiLmmI",
                            "https://www.youtube.com/watch?v=vmEHCJofslg"
                        ]
                    },
                    {
                        "title": "Data Visualization",
                        "description": "Learn Matplotlib and Seaborn for creating informative visualizations and exploratory data analysis.",
                        "estimated_duration": "1-2 weeks",
                        "resources": ["Matplotlib Gallery", "Seaborn Tutorial"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=3Xc3CA655Y4",
                            "https://www.youtube.com/watch?v=6GUZXDef2U0"
                        ]
                    },
                    {
                        "title": "Statistics for Data Science",
                        "description": "Learn descriptive statistics, probability, distributions, hypothesis testing, and correlation analysis.",
                        "estimated_duration": "3 weeks",
                        "resources": ["Khan Academy Statistics", "StatQuest"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=xxpc-HPKN28",
                            "https://www.youtube.com/watch?v=qBigTkBLU6g"
                        ]
                    },
                    {
                        "title": "First Data Analysis Project",
                        "description": "Complete an end-to-end data analysis project with real datasets from Kaggle or UCI repository.",
                        "estimated_duration": "2 weeks",
                        "resources": ["Kaggle", "UCI ML Repository"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=r-uOLxNrNk8",
                            "https://www.youtube.com/watch?v=xi0vhXFPegw"
                        ]
                    }
                ],
                "intermediate": [
                    {
                        "title": "Machine Learning Fundamentals",
                        "description": "Learn supervised and unsupervised learning, regression, classification, and clustering algorithms.",
                        "estimated_duration": "4 weeks",
                        "resources": ["Scikit-learn Documentation", "ML Course by Andrew Ng"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=7eh4d6sabA0",
                            "https://www.youtube.com/watch?v=ukzFI9rgwfU"
                        ]
                    },
                    {
                        "title": "Feature Engineering",
                        "description": "Master feature selection, scaling, encoding categorical variables, and handling missing data.",
                        "estimated_duration": "2 weeks",
                        "resources": ["Feature Engineering Guide", "Kaggle Learn"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=6WDFfaYtN6s",
                            "https://www.youtube.com/watch?v=3R-ADAg5XYY"
                        ]
                    },
                    {
                        "title": "SQL for Data Science",
                        "description": "Learn SQL queries, joins, aggregations, and database operations for data extraction and analysis.",
                        "estimated_duration": "2 weeks",
                        "resources": ["Mode SQL Tutorial", "SQLZoo"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=HXV3zeQKqGY",
                            "https://www.youtube.com/watch?v=7S_tz1z_5bA"
                        ]
                    },
                    {
                        "title": "Deep Learning Basics",
                        "description": "Introduction to neural networks, TensorFlow/PyTorch, and building simple deep learning models.",
                        "estimated_duration": "3 weeks",
                        "resources": ["TensorFlow Tutorial", "PyTorch Documentation"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=aircAruvnKk",
                            "https://www.youtube.com/watch?v=GIsg-ZUy0MY"
                        ]
                    },
                    {
                        "title": "Kaggle Competition Project",
                        "description": "Participate in a Kaggle competition to apply ML skills and learn from the community.",
                        "estimated_duration": "3-4 weeks",
                        "resources": ["Kaggle Competitions", "Kaggle Kernels"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=GJBOMWpLpTQ",
                            "https://www.youtube.com/watch?v=FloMHMOU5Bs"
                        ]
                    }
                ],
                "advanced": [
                    {
                        "title": "Advanced Deep Learning",
                        "description": "Master CNNs, RNNs, LSTMs, Transformers, and advanced architectures for computer vision and NLP.",
                        "estimated_duration": "4 weeks",
                        "resources": ["Deep Learning Specialization", "Papers with Code"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=CS4cs9xVecg",
                            "https://www.youtube.com/watch?v=kCc8FmEb1nY"
                        ]
                    },
                    {
                        "title": "Natural Language Processing",
                        "description": "Learn NLP techniques, word embeddings, BERT, GPT, and transformer models for text analysis.",
                        "estimated_duration": "3 weeks",
                        "resources": ["HuggingFace Course", "NLP with Transformers"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=8rXD5-xhemo",
                            "https://www.youtube.com/watch?v=SZorAJ4I-sA"
                        ]
                    },
                    {
                        "title": "MLOps & Model Deployment",
                        "description": "Learn model deployment, Docker, Kubernetes, ML pipelines, and production best practices.",
                        "estimated_duration": "3 weeks",
                        "resources": ["MLflow Documentation", "Kubeflow"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=6wWdNg0GMV4",
                            "https://www.youtube.com/watch?v=pXck7Bd4LH0"
                        ]
                    },
                    {
                        "title": "Big Data Technologies",
                        "description": "Master Spark, Hadoop, distributed computing, and processing large-scale datasets.",
                        "estimated_duration": "3 weeks",
                        "resources": ["Apache Spark Documentation", "Databricks"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=_C8kWso4ne4",
                            "https://www.youtube.com/watch?v=QaoJNXW6SQo"
                        ]
                    },
                    {
                        "title": "Research & Advanced Projects",
                        "description": "Work on cutting-edge projects, read research papers, and contribute to open-source ML projects.",
                        "estimated_duration": "Ongoing",
                        "resources": ["ArXiv", "Papers with Code", "GitHub"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=733m6qBH-jI",
                            "https://www.youtube.com/watch?v=ImLFlLjSveM"
                        ]
                    }
                ]
            },
            "Mobile Development": {
                "beginner": [
                    {
                        "title": "Programming Fundamentals",
                        "description": "Choose your path: Kotlin for Android or Swift for iOS. Learn basic programming concepts and syntax.",
                        "estimated_duration": "2-3 weeks",
                        "resources": ["Kotlin Documentation", "Swift Documentation"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=F9UC9DY-vIU",
                            "https://www.youtube.com/watch?v=comQ1-x2a1Q"
                        ]
                    },
                    {
                        "title": "UI/UX Design Basics",
                        "description": "Learn mobile UI/UX principles, Material Design (Android) or Human Interface Guidelines (iOS).",
                        "estimated_duration": "1-2 weeks",
                        "resources": ["Material Design", "Apple HIG"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=Qgbs1epAZWU",
                            "https://www.youtube.com/watch?v=RJnLd6fU2XE"
                        ]
                    },
                    {
                        "title": "First Mobile App",
                        "description": "Build your first simple app with activities/screens, buttons, and basic navigation.",
                        "estimated_duration": "2 weeks",
                        "resources": ["Android Studio", "Xcode"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=fis26HvvDII",
                            "https://www.youtube.com/watch?v=09TeUXjzpKs"
                        ]
                    },
                    {
                        "title": "Data Storage & APIs",
                        "description": "Learn local data storage (SQLite, Room) and making API calls to backend services.",
                        "estimated_duration": "2 weeks",
                        "resources": ["Room Database", "URLSession", "Retrofit"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=lwAvI3WDXBY",
                            "https://www.youtube.com/watch?v=5xVnqKhQFZs"
                        ]
                    },
                    {
                        "title": "Publish Your First App",
                        "description": "Learn app deployment to Google Play Store or Apple App Store, including guidelines and best practices.",
                        "estimated_duration": "1 week",
                        "resources": ["Play Console", "App Store Connect"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=cK0JYmHAkno",
                            "https://www.youtube.com/watch?v=j9QToZe4j3I"
                        ]
                    }
                ],
                "intermediate": [
                    {
                        "title": "Advanced UI Components",
                        "description": "Master RecyclerViews/TableViews, custom views, animations, and complex layouts.",
                        "estimated_duration": "3 weeks",
                        "resources": ["Android Developers", "SwiftUI Tutorial"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=Vyqz_-sJGFk",
                            "https://www.youtube.com/watch?v=F2ojC6TNwws"
                        ]
                    },
                    {
                        "title": "Architecture Patterns",
                        "description": "Learn MVVM, MVP, or Clean Architecture for scalable and maintainable mobile apps.",
                        "estimated_duration": "2 weeks",
                        "resources": ["Android Architecture Components", "iOS Architecture"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=I5c7fBgvkNY",
                            "https://www.youtube.com/watch?v=j2xNYfqL5aU"
                        ]
                    },
                    {
                        "title": "Firebase Integration",
                        "description": "Implement Firebase for authentication, real-time database, push notifications, and analytics.",
                        "estimated_duration": "2 weeks",
                        "resources": ["Firebase Documentation"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=fgdpvwEWJ9M",
                            "https://www.youtube.com/watch?v=p7QzLPzd-fU"
                        ]
                    },
                    {
                        "title": "Testing & Debugging",
                        "description": "Learn unit testing, UI testing, debugging tools, and performance optimization.",
                        "estimated_duration": "2 weeks",
                        "resources": ["JUnit", "XCTest"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=EkfVL5vCDmo",
                            "https://www.youtube.com/watch?v=jGRcObp94yw"
                        ]
                    },
                    {
                        "title": "Complex App Project",
                        "description": "Build a feature-rich app with multiple screens, data persistence, and third-party integrations.",
                        "estimated_duration": "4 weeks",
                        "resources": ["GitHub Awesome Mobile", "App Ideas"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=Hcey73IRjlg",
                            "https://www.youtube.com/watch?v=RijyKBfsrFw"
                        ]
                    }
                ],
                "advanced": [
                    {
                        "title": "Cross-Platform Development",
                        "description": "Learn React Native or Flutter to build apps for both iOS and Android with shared codebase.",
                        "estimated_duration": "4 weeks",
                        "resources": ["React Native Docs", "Flutter Documentation"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=0-S5a0eXPoc",
                            "https://www.youtube.com/watch?v=1ukSR1GRtMU"
                        ]
                    },
                    {
                        "title": "Advanced Performance",
                        "description": "Master performance optimization, memory management, battery efficiency, and profiling tools.",
                        "estimated_duration": "2 weeks",
                        "resources": ["Android Profiler", "Instruments"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=Qfo5fdoXrTU",
                            "https://www.youtube.com/watch?v=g5JrOALcRo0"
                        ]
                    },
                    {
                        "title": "CI/CD for Mobile",
                        "description": "Set up continuous integration and deployment pipelines with Fastlane, GitHub Actions, or Bitrise.",
                        "estimated_duration": "2 weeks",
                        "resources": ["Fastlane Documentation", "GitHub Actions"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=rZgkzTdqpy4",
                            "https://www.youtube.com/watch?v=HOLKbrUBqSQ"
                        ]
                    },
                    {
                        "title": "Security Best Practices",
                        "description": "Learn mobile security, encryption, secure storage, API security, and common vulnerabilities.",
                        "estimated_duration": "2 weeks",
                        "resources": ["OWASP Mobile Security", "Security Guidelines"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=IMNcBmp5PT8",
                            "https://www.youtube.com/watch?v=BLGFriOKz6U"
                        ]
                    },
                    {
                        "title": "Production App Development",
                        "description": "Build and launch a production-ready app with proper architecture, testing, and monetization strategy.",
                        "estimated_duration": "6-8 weeks",
                        "resources": ["App Business Model", "Marketing Strategies"],
                        "video_links": [
                            "https://www.youtube.com/watch?v=GkPbf-0DmwA",
                            "https://www.youtube.com/watch?v=Q4F0y2CQCxU"
                        ]
                    }
                ]
            }
        }
    
    def generate_roadmap(self, field, skill_level, interests=None):
        """
        Generate a personalized learning roadmap based on user inputs
        """
        field = field.strip()
        skill_level = skill_level.lower().strip()
        
        # Get base roadmap from templates
        if field in self.roadmap_templates and skill_level in self.roadmap_templates[field]:
            base_steps = self.roadmap_templates[field][skill_level].copy()
            
            # Customize based on interests if provided
            if interests:
                # Add interest-specific customization
                base_steps = self._customize_by_interests(base_steps, interests, field)
            
            return {
                "title": f"{field} - {skill_level.capitalize()} Level",
                "field": field,
                "skill_level": skill_level,
                "steps": base_steps,
                "total_duration": self._calculate_total_duration(base_steps)
            }
        else:
            # Generate generic roadmap
            return self._generate_generic_roadmap(field, skill_level, interests)
    
    def _customize_by_interests(self, steps, interests, field):
        """
        Customize roadmap steps based on user interests
        """
        # This is where you can add logic to reorder or emphasize certain steps
        # based on user interests
        return steps
    
    def _calculate_total_duration(self, steps):
        """
        Calculate estimated total time for completing the roadmap
        """
        total_weeks = 0
        for step in steps:
            duration = step.get('estimated_duration', '1 week')
            if 'week' in duration.lower():
                # Extract number of weeks
                nums = [int(s) for s in duration.split() if s.isdigit()]
                if nums:
                    total_weeks += max(nums)
        
        if total_weeks > 0:
            months = total_weeks // 4
            remaining_weeks = total_weeks % 4
            if months > 0 and remaining_weeks > 0:
                return f"{months} months {remaining_weeks} weeks"
            elif months > 0:
                return f"{months} months"
            else:
                return f"{total_weeks} weeks"
        return "Variable"
    
    def _generate_generic_roadmap(self, field, skill_level, interests):
        """
        Generate a generic roadmap for fields not in templates
        """
        generic_steps = [
            {
                "title": f"Introduction to {field}",
                "description": f"Learn the fundamental concepts and basics of {field}. Understand the core principles and terminology.",
                "estimated_duration": "2-3 weeks",
                "resources": ["Online tutorials", "Documentation", "Books"],
                "video_links": ["https://www.youtube.com/results?search_query=" + field.replace(" ", "+")]
            },
            {
                "title": "Core Skills Development",
                "description": f"Build essential skills required for {field}. Practice with hands-on projects and exercises.",
                "estimated_duration": "4-6 weeks",
                "resources": ["Practice platforms", "Project ideas"],
                "video_links": ["https://www.youtube.com/results?search_query=" + field.replace(" ", "+") + "+tutorial"]
            },
            {
                "title": "Practical Projects",
                "description": f"Apply your knowledge by building real-world projects in {field}.",
                "estimated_duration": "3-4 weeks",
                "resources": ["GitHub", "Project portfolios"],
                "video_links": ["https://www.youtube.com/results?search_query=" + field.replace(" ", "+") + "+projects"]
            },
            {
                "title": "Advanced Concepts",
                "description": f"Dive deeper into advanced topics and specialized areas of {field}.",
                "estimated_duration": "4-6 weeks",
                "resources": ["Advanced courses", "Research papers"],
                "video_links": ["https://www.youtube.com/results?search_query=" + field.replace(" ", "+") + "+advanced"]
            },
            {
                "title": "Professional Development",
                "description": f"Build a professional portfolio, network with others, and prepare for career opportunities in {field}.",
                "estimated_duration": "Ongoing",
                "resources": ["LinkedIn", "Professional communities"],
                "video_links": ["https://www.youtube.com/results?search_query=" + field.replace(" ", "+") + "+career"]
            }
        ]
        
        return {
            "title": f"{field} - {skill_level.capitalize()} Level",
            "field": field,
            "skill_level": skill_level,
            "steps": generic_steps,
            "total_duration": self._calculate_total_duration(generic_steps)
        }
    
    def get_available_fields(self):
        """
        Return list of available career fields
        """
        return list(self.roadmap_templates.keys())
    
    def get_skill_levels(self):
        """
        Return available skill levels
        """
        return ["beginner", "intermediate", "advanced"]