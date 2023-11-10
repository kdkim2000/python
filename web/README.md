# 파이썬 웹 프로그램 만들기

## backend 

### 파이썬 프레이 워크

파이썬의 프레임워크를 이해하기 위해선 먼저 '프레임워크'가 무엇인지부터 알아야 합니다. 프레임워크란 특정 프로그램을 개발하기 위해 제공되는 라이브러리와 도구의 집합을 말합니다. 특히 웹 개발 프레임워크는 웹 사이트를 생성하고 관리하기 위한 구조를 제공하는 도구입니다.

파이썬에서는 다양한 프레임워크가 있지만, 가장 널리 사용되는 것들은 Django와 Flask입니다.

Django: 이 프레임워크는 "배터리 포함"이라는 철학을 가지고 있어, 개발자가 필요로 하는 거의 모든 기능을 내장하고 있습니다. 즉, 데이터베이스 인터페이스, 관리자 패널, ORM(Object-relational mapping) 등을 제공하므로 개발 시간을 크게 단축시킬 수 있습니다. 그러나 이런 특징 때문에 때로는 Django가 너무 무겁다는 비판도 있습니다.

Flask: 이 프레임워크는 '마이크로' 프레임워크로, 최소한의 기능만을 제공합니다. 하지만, 그로 인해 개발자가 필요한 기능을 자유롭게 추가하고, 원하는 대로 애플리케이션을 구성할 수 있습니다. 또한, 복잡하지 않은 웹 사이트를 빠르게 개발하는 데 적합합니다.

이 외에도 파이썬에는 다양한 프레임워크가 있으니, 개발하고자 하는 프로젝트의 목적과 요구사항에 맞게 선택하시면 됩니다. 그리고 각 프레임워크의 공식 문서를 참고하시면 좀 더 깊이 있는 이해를 할 수 있습니다.

| 항목 | Django | Flask |
| --- | --- | --- |
| 철학 | "배터리 포함" - 필요한 모든 기능을 내장 | "마이크로" - 최소한의 기능만 제공 |
| 복잡성 | 복잡한 기능과 구조, 높은 학습 곡선 | 간단하고 직관적, 낮은 학습 곡선 |
| 확장성 | 기본적으로 많은 기능을 제공하므로 확장성이 높음 | 필요한 기능을 직접 추가해야 하므로 확장성이 낮음 |
| 적합한 프로젝트 | 크고 복잡한 웹 애플리케이션 | 작고 간단한 웹 애플리케이션 |
| 관리 도구 | 관리자 패널 제공 | 관리 도구 없음 |
| ORM 지원 | Django ORM 제공 | SQLAlchemy 등을 사용하여 별도 구성 필요 |