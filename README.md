# AI-Driven Tool for Crop Disease Detection in South Africa

## Project Overview
This project aims to develop an AI-powered tool to detect crop diseases in South Africa's agricultural sector. The system leverages a Convolutional Neural Network (CNN) trained on datasets of diseased crop images. A user-friendly web and mobile interface allows farmers and stakeholders to upload images and receive accurate predictions along with actionable recommendations.

## Table of Contents
1. [Introduction](#introduction)
2. [Repository Layer](#repository-layer)
3. [Design Decisions](#design-decisions)
4. [Future-Proofing](#future-proofing)
5. [Directory Structure](#directory-structure)
6. [How to Run the Project](#how-to-run-the-project)

---

## Introduction
The system is designed to:
- Detect five major crop diseases: Maize Streak Virus, Citrus Black Spot, Fusarium Wilt, Late Blight, and Downy Mildew.
- Provide rapid and accurate feedback through a trained CNN model.
- Offer a simple and intuitive interface for users to interact with the system.

---

## Repository Layer
The repository layer abstracts storage details behind a generic interface, enabling easy swapping of storage backends. It currently supports an in-memory `HashMap` but is designed to accommodate future storage mechanisms like databases or filesystems.

### Key Features
- **Generic Repository Interface**: Supports CRUD operations for all domain entities (e.g., `Image`, `Prediction`).
- **Entity-Specific Repositories**: Extend the generic interface for specific entities (e.g., `ImageRepository`).
- **Factory Pattern**: Allows dynamic switching between storage implementations (e.g., in-memory, database).

---

## Design Decisions
- **Generics**: Used to avoid duplication across entity repositories (e.g., `Repository<T, ID>`).
- **Factory Pattern**: Chosen over Dependency Injection (DI) for simplicity and flexibility in managing storage implementations.
- **In-Memory Storage**: Implemented first for simplicity and ease of testing.

---

## Future-Proofing
The repository layer is designed to support additional storage mechanisms:
- **Filesystem Storage**: Serialize objects to JSON or XML files.
- **SQL/NoSQL Databases**: Integrate with MySQL, MongoDB, etc.
- **External APIs**: Fetch/store data via REST APIs.

---

## Directory Structure
