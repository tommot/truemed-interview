# Truemed Interview Repo

## Senior Engineer

This project is meant to assess your ability to perform at a senior level at Truemed. Specifically, we expect senior developers to own large projects from end-to-end, even if some pieces are outside of your expertise. This often involves some research & planning before jumping straight to implementation (and course-correcting as you come across new information).

### Constraints

- Please don’t spend more than 3 hours on this project. We expect a barely-functional Proof-of-Concept and a write-up of next steps.

### Goal

Your mission is to implement the Truemed payment method on [this checkout page](https://www.loom.com/share/eb3c03c95ec4456282a5f5e0f486fff0?sid=deb7ff13-d26c-499c-be18-d520a1a5290a). Your priorities are:

P0 (most important):

- Get a Proof-of-Concept UX in place (redirect to Truemed for payment capture when a user presses the "Pay with HSA / FSA" button)

P1 (nice-to-have):

- Document next steps to improve the implementation

Out of Scope (don't do these, not even as a bonus):

- Any improvements to the store whatsoever
- Anything that requires a Django migration
- Robust order-tracking

### How can I get started with the Truemed API?

- [Truemed developer docs](https://developers.truemed.com)
  - use `https://dev-api.truemed.com` as the base URL for our sandbox environment
- You should have an email with sandbox credentials

## Getting Started

- Create a personal, private fork of this repository
- Clone it locally
- Get the frontend & backend running (see readme files in each folder)

## Submission

It's important to make sure your submission is only visible to people with collaborator access to your private repo. Do not make a pull request against our main repository. Instead:

- Create a new branch (from your private fork's main branch) with your changes
- Create a Pull Request against your own fork's main branch
- Add `john@truemed.com` as an outside collaborator and email him a link to your Pull Request.

## FAQ

### What is this repository?

- A fork of [this project](https://github.com/kkosiba/ecommerce-backend?tab=readme-ov-file)
- Modified quickly to work as an interview starter project
- There are some...quirks (class-based React, UK currency & address validation, etc...)

### What are the expectations, exactly?

- Write great functions.
- Write a great plan for next steps.
- Don't refactor anything.

### What does a valid UK mailing address look like?

- https://chatgpt.com/share/bcd2d4e4-28e6-4db9-9081-5c02cb496e4a

### Where should I start writing code?

- `backend/payments/views.py`

### How should I handle secrets?

- Just hard-code all keys in `backend/src/settings/base.py`
