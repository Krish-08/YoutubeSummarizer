
from youtube_transcript_api import YouTubeTranscriptApi

import json

from youtube_transcript_api.formatters import TextFormatter

import summarizer
class gettranscript:
    def __init__(self):
        pass
    
    
    
    def StringTime(self,time):
        time = (int)(time)
        return (str)(time // 60) + ":" + (str)(time % 60) 

    
    def transcript(self,link):
        
        try:
            obj=summarizer.summary()
            if("youtube" in link):
                id = (link.split('=')[1]).split("&")[0]
            else:
                id=link.split('/')[3]
            print(id)
            script=YouTubeTranscriptApi.get_transcript(id)
            formatter = TextFormatter()
            scriptText = formatter.format_transcript(script)
            # print("before Summary")
            print(len(script))
            print(len(scriptText))
            print(len(obj.getSummary(scriptText,0.1)))
            max_duration=max(30,script[-1]["start"]//5)
            print(max_duration)
            ctr,end,start=0,0,0
            summaryContent=[]
            blockText=""
            while ctr<len(script):
                if(end-start<=max_duration):
                    end=script[ctr]["start"]+script[ctr]["duration"]
                    blockText+=script[ctr]["text"]+" "
                    blockText+=" "
                    
                
                else:

                    print("in summary loop")
                    print(len(blockText))
                    summaryContent.append(
                        {
                            "start":self.StringTime(start),
                            "end":self.StringTime(end),
                            "text":obj.getSummary(blockText,0.1)
                        }
                    )
                    start=end
                    end=script[ctr]["start"]+script[ctr]["duration"]
                    blockText=script[ctr]["text"]
                   
                ctr+=1
            summaryContent.append(
                {
                    "start":self.StringTime(start),
                    "end":self.StringTime(end),
                    "text":obj.getSummary(blockText,0.1)
                }
                
            )
            
            return json.dumps(summaryContent)
        
        except Exception as e:
            
            print(e)

        

