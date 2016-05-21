# Notes on Better Embedded Systems [TW-zh]
這本書的作者是我在2015年夏天，在成大上嵌入式系統暑期課程時聽Jersv大大提到作者後找來看的。原書[Amazon Link](http://www.amazon.com/dp/0984449000/ref=as_sl_pc_tf_lc?tag=embedsyste0a-20&camp=14573&creative=327641&linkCode=as1&creativeASIN=0984449000&adid=0WTBT96KGSYSW8D9ZBW2&&ref-refURL=http%3A%2F%2Fbetterembsw.blogspot.tw%2F)。那個時候提到的是作者Philip Koopman教授，為TOYOTA煞車故障車禍事故查找原因的分析報告。

整本書看起來在各種軟體開發皆適用。
因為每次我都是要還書了才會把書拿起來看，今天就用力為這本書寫多些筆記。
This book distills the experience of more than 90 design reviews on real embedded systems into a set of bite-size lessons learned in the areas of software development process, requirements, architecture, design, implementation, verification & validation, and critical system properties.
Each chapter describes an area that tends to be a problem in embedded system design, symptoms that tend to indicate you need to make changes, the risks of not fixing problems in this area, and concrete ways to make your embedded system software better. Each of the 29 chapters is self-sufficient, permitting developers with a busy schedule to cherry-pick the best ideas to make their systems better right away.

If you are relatively new to the area but have already learned the basics, this book will be an invaluable asset for taking your game to the next level. If you are experienced, this book provides a way to fill in any gaps. Once you have mastered this material, the book will serve as a source of reminders to make sure you haven't forgotten anything as you plan your next project. The product image of the back of the book lists the chapters.


# Topics
1. Introduction
## Software Development Process
2. Written Development Plan
3. How Much Paper is Enough
4. How Much Paper is Too Much
## Requirements & architecture
5. Written Requirements
6. Measurable Requirements
7. Tracing Requirements to testing
8. Non-Functional Requirements
9. Requirements Churn
10. Software architecture
11. Modularity
## design
12. Software design
13. Statecharts and modes
14. Real time
15. User Interface design
## implementation
16. How Much Assembly Language Is Enough
17. Coding Style
18. The Cost Of Nearly Full Resources
19. Global Variables Are Evil
20. Mutexes and Data Access Concurrency
## Verification & validation
21. Static Checking and Compiler Warnings
22. Peer Reviews
23. Testing and Test plans
24. Issue Tracking & Analysis
25. Run-Time Error logs
## Critical System properties
26. Dependability
27. Security
28. Safety
29. Watchdog Timers
30. System Reset
