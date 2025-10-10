class Attendee{
  constructor(name,email){
    this.name=name;
    this.email=email;
  }
}
class Event{
    constructor(eventName,date){
    this.eventName=eventName;
    this.date=date;
    this.registeredAttendees =new Set();
  }
  register(attendee){
    if(this.registeredAttendees.has(attendee.email)){
      return false;
    }
    else{
      this.registeredAttendees.add(attendee.email);
      return true;
    }
  }
}
let EventManager={
  events : new Map(),
  createEvent : function(event){
      this.events.set(event.eventName,event);
  },
  getEventSummary : function (eventName){
    if(!this || !this.events){
      return "ERROR : INVALID_CONTEXT";
    }
    const event = this.events.get(eventName);
    if(event){
      return `SUMMARY : ${event.eventName}/${event.registeredAttendees.size}`;
    }
    return `ERROR : NOT_FOUND`;
  }
};
let jsConf=new Event("JS Conference",`2025-12-01`);
let pythonSummit=new Event(`Python Summit`,`2025-12-15`);
EventManager.createEvent(jsConf);
EventManager.createEvent(pythonSummit);
let Hiya_B=new Attendee("Hiya Batt","hiya@example.com");
let Kunal_B=new Attendee("Kunal Bhosikar","kunal.example.com");
jsConf.register(Hiya_B);
jsConf.register(Kunal_B);
jsConf.register(Hiya_B);
pythonSummit.register(Kunal_B);