#!groovy
pipeline {
  agent any
  stages{
    stage ('Checkout')
    node('slave') {
      deleteDir()
      checkout scm
    }
  }
}
