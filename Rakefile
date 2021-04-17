require "rubygems"

desc "Deploy docs directory to Github Pages"
task :deploy, [:arg1] do |t, args|
  puts "## Deploying to Github Pages"

  puts "## Generating site"
  system "grunt build"

  puts "## Deleting current docs directory"
  system "rmdir docs /s"

  puts "## Copying _site into new docs directory"
  system "xcopy _site docs /s"

  system "git add docs"

  message = "#{Time.now.utc}: #{args[:arg1]}"
  puts "## Commiting: #{message}"
  system "git commit -m \"#{message}\""

  puts "## Pushing generated site"
  system "git push"

  puts "## Deploy Complete!"

  puts "## Deploy Complete!"
end