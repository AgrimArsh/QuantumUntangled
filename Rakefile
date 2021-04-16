require "rubygems"

desc "Deploy to Github Pages"
task :deploy do
  puts "## Deploying to Github Pages"

  puts "## Generating site"
  system "grunt build"

  puts "## Deleting current docs directory"
  system "rmdir docs /s"

  puts "## Copying _site into new docs directory"
  system "xcopy _site docs /s"

  system "git add -A"

  message = "Site updated at #{Time.now.utc}"
  puts "## Commiting: #{message}"
  system "git commit -m \"#{message}\""

  puts "## Pushing generated site"
  system "git push"

  puts "## Deploy Complete!"
end