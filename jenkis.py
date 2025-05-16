pipeline{
agent any{
stages{
stage('testing){
step{echo "hi"}}
stage('deploy'){step {echo "deployed'"}}}}
