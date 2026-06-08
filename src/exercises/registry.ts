import { ExerciseDefinition } from './types';
import { 
  basicPayloadBuilder, 
  mcqPayloadBuilder, 
  assemblyPayloadBuilder, 
  recallPayloadBuilder 
} from './factories';
import { 
  exactMatchValidator, 
  mcqValidator, 
  assemblyValidator, 
  fuzzyMatchValidator 
} from './validators';
import { defaultCompletionHandler } from './completion';

/**
 * The Central Exercise Registry.
 * Defines the contract for all 12 supported exercise types.
 */
export const ExerciseRegistry: Record<string, ExerciseDefinition> = {
  Listen: {
    metadata: { id: 'Listen', name: 'Listening', category: 'Recognition', difficulty: 'Beginner' },
    payloadBuilder: mcqPayloadBuilder,
    validator: exactMatchValidator, // Audio playback is binary success usually
    completionHandler: defaultCompletionHandler
  },
  ListenChoose: {
    metadata: { id: 'ListenChoose', name: 'Listen & Choose', category: 'Recognition', difficulty: 'Beginner' },
    payloadBuilder: mcqPayloadBuilder,
    validator: mcqValidator,
    completionHandler: defaultCompletionHandler
  },
  Match: {
    metadata: { id: 'Match', name: 'Matching', category: 'Recognition', difficulty: 'Beginner' },
    payloadBuilder: mcqPayloadBuilder,
    validator: mcqValidator,
    completionHandler: defaultCompletionHandler
  },
  BuildSentence: {
    metadata: { id: 'BuildSentence', name: 'Sentence Builder', category: 'Recall', difficulty: 'Intermediate' },
    payloadBuilder: assemblyPayloadBuilder,
    validator: assemblyValidator,
    completionHandler: defaultCompletionHandler
  },
  Recall: {
    metadata: { id: 'Recall', name: 'Memory Recall', category: 'Recall', difficulty: 'Intermediate' },
    payloadBuilder: recallPayloadBuilder,
    validator: exactMatchValidator,
    completionHandler: defaultCompletionHandler
  },
  Dictation: {
    metadata: { id: 'Dictation', name: 'Dictation', category: 'Production', difficulty: 'Advanced' },
    payloadBuilder: basicPayloadBuilder,
    validator: exactMatchValidator,
    completionHandler: defaultCompletionHandler
  },
  Speaking: {
    metadata: { id: 'Speaking', name: 'Speaking', category: 'Production', difficulty: 'Advanced' },
    payloadBuilder: basicPayloadBuilder,
    validator: fuzzyMatchValidator,
    completionHandler: defaultCompletionHandler
  },
  Reading: {
    metadata: { id: 'Reading', name: 'Reading', category: 'Recognition', difficulty: 'Beginner' },
    payloadBuilder: basicPayloadBuilder,
    validator: exactMatchValidator,
    completionHandler: defaultCompletionHandler
  },
  Conversation: {
    metadata: { id: 'Conversation', name: 'Conversation', category: 'Application', difficulty: 'Advanced' },
    payloadBuilder: basicPayloadBuilder,
    validator: mcqValidator, // User choices
    completionHandler: defaultCompletionHandler
  },
  Review: {
    metadata: { id: 'Review', name: 'SRS Review', category: 'Recall', difficulty: 'Intermediate' },
    payloadBuilder: basicPayloadBuilder,
    validator: exactMatchValidator,
    completionHandler: defaultCompletionHandler
  },
  Assembly: {
    metadata: { id: 'Assembly', name: 'Word Assembly', category: 'Recall', difficulty: 'Intermediate' },
    payloadBuilder: assemblyPayloadBuilder,
    validator: assemblyValidator,
    completionHandler: defaultCompletionHandler
  },
  Spelling: {
    metadata: { id: 'Spelling', name: 'Spelling', category: 'Production', difficulty: 'Advanced' },
    payloadBuilder: basicPayloadBuilder,
    validator: exactMatchValidator,
    completionHandler: defaultCompletionHandler
  }
};
