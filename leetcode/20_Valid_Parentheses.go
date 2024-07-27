package main

import (
  "fmt"
  "errors"
)

type Stack struct {
	values []string
}

func (s *Stack) Push(value string) {
	s.values = append(s.values, value)
}

func (s *Stack) Pop() (string, error) {
  l := len(s.values)
  if l == 0 {
    return "", errors.New("There are no values in the stack.")
  }
  value := s.values[l-1]
  s.values = s.values[:l-1]
  return value, nil
}

var brackets = map[string]string{
  "[": "]",
  "{": "}",
  "(": ")",
}

func isValid(s string) bool {
  if len(s) < 2 {
    return false
  }
  stack := Stack{}
  for _, bracket := range s {
    stringBracket := string(bracket)
    // check if sequence starts with correct bracket
    if _, ok := brackets[stringBracket]; ok {
      stack.Push(stringBracket)
    } else {
      openBracket, err := stack.Pop()
      if err != nil {
        return false
      }
      closeBracket := brackets[openBracket]
      if stringBracket != closeBracket {
        return false
      }
    }
  }
  if len(stack.values) > 0 {
    return false
  }
  return true
}

func main() {
  inputs := []string{
  "[()]{}",
  "[{()}]{({{{()}}})}",
  "[[(){()}]]",
  "[({)]}",
  "[[",
  "){",
  }
  for _, input := range inputs {
    result := isValid(input)
    fmt.Println(result)
  }
}
